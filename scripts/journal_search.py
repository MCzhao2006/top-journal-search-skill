#!/usr/bin/env python3
"""Discover article candidates in top journals via Crossref.

This helper is intentionally metadata-first. Results should be verified on the
publisher's official article page before using them as substantive evidence.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Any

JOURNALS = {
    "nature": {
        "title": "Nature",
        "issn": "1476-4687",
        "official": "https://www.nature.com/nature/",
    },
    "science": {
        "title": "Science",
        "issn": "1095-9203",
        "official": "https://www.science.org/journal/science",
    },
    "lancet": {
        "title": "The Lancet",
        "issn": "1474-547X",
        "official": "https://www.thelancet.com/",
    },
    "nejm": {
        "title": "New England Journal of Medicine",
        "issn": "1533-4406",
        "official": "https://www.nejm.org/",
    },
    "jama": {
        "title": "JAMA",
        "issn": "1538-3598",
        "official": "https://jamanetwork.com/journals/jama",
    },
    "cell": {
        "title": "Cell",
        "issn": "1097-4172",
        "official": "https://www.cell.com/cell/home",
    },
    "pnas": {
        "title": "Proceedings of the National Academy of Sciences",
        "issn": "1091-6490",
        "official": "https://www.pnas.org/",
    },
}

CROSSREF = "https://api.crossref.org/works"
LOCAL_SOCKS_PORTS = (1024, 7890, 1080, 10808)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Search top-journal metadata via Crossref.")
    p.add_argument("--journal", choices=sorted(JOURNALS), help="Target flagship journal.")
    p.add_argument("--query", help="Topic, title words, author, or other bibliographic query.")
    p.add_argument("--doi", help="Exact DOI lookup. Journal is optional for DOI mode.")
    p.add_argument("--from-date", help="Earliest publication date, YYYY-MM-DD.")
    p.add_argument("--until-date", help="Latest publication date, YYYY-MM-DD.")
    p.add_argument("--limit", type=int, default=10, help="Maximum records (1-100).")
    p.add_argument("--sort", choices=("relevance", "published"), default="relevance")
    p.add_argument("--format", choices=("markdown", "json"), default="markdown")
    p.add_argument("--try-local-socks", action="store_true", help="After direct failure, try fixed localhost SOCKS5 ports.")
    p.add_argument("--timeout", type=float, default=10.0)
    args = p.parse_args()
    if not args.doi and not args.query:
        p.error("provide --query or --doi")
    if not args.doi and not args.journal:
        p.error("--journal is required for topic/title searches")
    if not 1 <= args.limit <= 100:
        p.error("--limit must be between 1 and 100")
    return args


def _fetch_direct(url: str, timeout: float) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "top-journal-search-skill/1.0 (mailto:example@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _fetch_socks(url: str, timeout: float) -> bytes:
    try:
        import requests  # type: ignore
    except Exception as exc:
        raise RuntimeError("SOCKS fallback needs requests plus PySocks (e.g. requests[socks]).") from exc

    last: Exception | None = None
    for port in LOCAL_SOCKS_PORTS:
        proxy = f"socks5h://127.0.0.1:{port}"
        try:
            r = requests.get(
                url,
                timeout=timeout,
                headers={"User-Agent": "top-journal-search-skill/1.0"},
                proxies={"http": proxy, "https": proxy},
            )
            r.raise_for_status()
            return r.content
        except Exception as exc:  # fixed localhost list only
            last = exc
    raise RuntimeError(f"all fixed localhost SOCKS attempts failed: {last}")


def fetch_json(url: str, timeout: float, try_local_socks: bool) -> Any:
    try:
        raw = _fetch_direct(url, timeout)
    except Exception as direct_exc:
        if not try_local_socks:
            raise RuntimeError(f"direct request failed: {direct_exc}") from direct_exc
        raw = _fetch_socks(url, timeout)
    return json.loads(raw.decode("utf-8"))


def build_url(args: argparse.Namespace) -> str:
    if args.doi:
        doi = args.doi.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        return f"{CROSSREF}/{urllib.parse.quote(doi, safe='')}"

    meta = JOURNALS[args.journal]
    filters = [f"issn:{meta['issn']}"]
    if args.from_date:
        filters.append(f"from-pub-date:{args.from_date}")
    if args.until_date:
        filters.append(f"until-pub-date:{args.until_date}")

    params = {
        "query.bibliographic": args.query,
        "filter": ",".join(filters),
        "rows": str(args.limit),
        "select": "DOI,title,author,published-print,published-online,created,URL,container-title,type,ISSN,publisher",
    }
    if args.sort == "published":
        params["sort"] = "published"
        params["order"] = "desc"
    return f"{CROSSREF}?{urllib.parse.urlencode(params)}"


def first(value: Any, default: str = "") -> str:
    if isinstance(value, list) and value:
        return str(value[0])
    if value is None:
        return default
    return str(value)


def date_from_parts(obj: dict[str, Any], key: str) -> str:
    parts = obj.get(key, {}).get("date-parts", [])
    if not parts or not parts[0]:
        return ""
    nums = list(parts[0]) + [1, 1]
    y, m, d = nums[:3]
    try:
        return datetime(int(y), int(m), int(d)).date().isoformat()
    except Exception:
        return "-".join(str(x) for x in parts[0])


def authors(item: dict[str, Any]) -> str:
    out = []
    for a in item.get("author", [])[:8]:
        name = " ".join(x for x in [a.get("given", ""), a.get("family", "")] if x).strip()
        if name:
            out.append(name)
    if len(item.get("author", [])) > 8:
        out.append("et al.")
    return ", ".join(out)


def normalize(item: dict[str, Any]) -> dict[str, Any]:
    date = date_from_parts(item, "published-online") or date_from_parts(item, "published-print") or date_from_parts(item, "created")
    doi = str(item.get("DOI", ""))
    return {
        "title": first(item.get("title")),
        "journal": first(item.get("container-title")),
        "date": date,
        "doi": doi,
        "doi_url": f"https://doi.org/{doi}" if doi else "",
        "authors": authors(item),
        "type": str(item.get("type", "")),
        "publisher": str(item.get("publisher", "")),
        "crossref_url": str(item.get("URL", "")),
    }


def extract_items(payload: Any) -> list[dict[str, Any]]:
    msg = payload.get("message", {})
    if "items" in msg:
        return [normalize(x) for x in msg.get("items", [])]
    if msg:
        return [normalize(msg)]
    return []


def emit_markdown(items: list[dict[str, Any]], journal: str | None) -> None:
    if journal:
        meta = JOURNALS[journal]
        print(f"Target: {meta['title']} | Official: {meta['official']}")
    print("Verification note: Crossref is for candidate discovery; verify substantive claims on the publisher page.\n")
    if not items:
        print("No records found.")
        return
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['title'] or '[untitled]'}")
        print(f"   Journal: {item['journal'] or '-'}")
        print(f"   Date: {item['date'] or '-'} | Type: {item['type'] or '-'}")
        if item["authors"]:
            print(f"   Authors: {item['authors']}")
        if item["doi"]:
            print(f"   DOI: {item['doi']} | {item['doi_url']}")
        print()


def main() -> int:
    args = parse_args()
    try:
        payload = fetch_json(build_url(args), args.timeout, args.try_local_socks)
        items = extract_items(payload)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(items, ensure_ascii=False, indent=2))
    else:
        emit_markdown(items, args.journal)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
