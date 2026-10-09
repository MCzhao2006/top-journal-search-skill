# Network Access and Failure Handling

## Direct access first

Try the official publisher site normally. Use a modest request rate and avoid repeated reloads.

If the site requires JavaScript, blocks automated requests, or returns incomplete HTML, switch to a browser/search tool or use structured bibliographic metadata for discovery and return to the publisher page for verification when possible.

## Local SOCKS fallback

如果直接访问失败,尝试使用socks5://127.0.0.1:的常见端口,比如1024,7890等

Interpret this as an **optional localhost fallback only when the runtime/user intentionally provides such a proxy**. Reasonable fixed ports include `1024`, `7890`, `1080`, and `10808`.

Safety and reliability rules:

- Try direct access before any proxy.
- Only try `127.0.0.1`; never scan a LAN, public IP range, or arbitrary remote proxy list.
- Use short timeouts.
- Stop after the small configured list of ports.
- Do not route credentials, session cookies, institutional login tokens, or other secrets through an unknown proxy.
- If the proxy is user-managed, prefer `socks5h://127.0.0.1:<port>` where supported so DNS resolution also follows the proxy.
- If SOCKS support is unavailable, do not install packages silently; explain the dependency or use another available network/search path.

## Paywalls and access controls

Do not bypass:

- subscription gates
- institutional authentication
- CAPTCHAs
- anti-bot controls
- robots or explicit automated-access restrictions

Instead use, in order:

1. accessible abstract/summary on the publisher site
2. PubMed / Europe PMC for biomedical abstracts and indexing
3. Crossref metadata for DOI/title/authors/date
4. author repository or legally available open-access version when discoverable
5. general web discovery restricted to reputable sources

State clearly when only metadata or an abstract was available.
