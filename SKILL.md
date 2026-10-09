---
name: top-journal-search
description: 搜索、定位、核验并综合来自顶尖科学与医学期刊网站的信息，专为 Nature、Science (AAAS)、The Lancet、NEJM、JAMA、Cell 与 PNAS 提供路由。用于用户要求查找论文、在顶刊网站搜索、按标题/作者/DOI/主题/日期定位文章、跨这些期刊比较证据、核验文章元数据或更正、识别近期论文，或从出版商页面提取有来源依据的事实时。优先使用官方出版商页面，仅将书目数据库作为发现/回退辅助，并明确区分旗舰期刊与其期刊家族。 Search, locate, verify, and synthesize information from leading scientific and medical journal websites, with dedicated routing for Nature, Science (AAAS), The Lancet, NEJM, JAMA, Cell, and PNAS. Use when the user asks to find papers, search a top-journal website, locate an article by title/author/DOI/topic/date, compare evidence across these journals, verify article metadata or corrections, identify recent papers, or extract source-grounded facts from publisher pages. Prefer official publisher pages, use bibliographic databases only as discovery/fallback aids, and clearly distinguish flagship journals from their journal families.
---

# Top Journal Search

将本 Skill 用作高影响力期刊网站的搜索与核验路由。优先把出版商页面当作文章身份与文章级事实的首选来源；当出版商搜索较弱或被阻断时，再用 Crossref、PubMed、Europe PMC、OpenAlex 或其他书目索引来发现候选。  
Use this skill as a search-and-verification router for high-impact journal websites. Treat publisher pages as the preferred source for article identity and article-level facts; use Crossref, PubMed, Europe PMC, OpenAlex, or other bibliographic indexes to discover candidates when publisher search is weak or blocked.

## 核心工作流 / Core workflow

1. **搜索前先确定范围。** / **Resolve scope before searching.**
   - 未限定的期刊名默认解释为旗舰刊：`Nature`、`Science`、`The Lancet`、`NEJM`、`JAMA`、`Cell` 或 `PNAS`。  
     Interpret an unqualified journal name as the flagship journal: `Nature`, `Science`, `The Lancet`, `NEJM`, `JAMA`, `Cell`, or `PNAS`.
   - 仅当用户说 “Nature family”、“Science journals”、“Lancet family”、“JAMA Network”、“Cell Press” 等时，才扩展到出版商家族。  
     Expand to a publisher family only when the user says “Nature family”, “Science journals”, “Lancet family”, “JAMA Network”, “Cell Press”, etc.
   - 保留用户约束：日期范围、作者、文章类型、领域、DOI、开放获取要求，或 “最新”。  
     Preserve user constraints: date range, author, article type, field, DOI, open-access requirement, or “latest”.

2. **对查询进行分类。** / **Classify the lookup.**
   - 精确标题 / DOI / 引用 -> 精确查找。  
     Exact title / DOI / citation -> exact lookup.
   - 作者 + 年份 -> 作者查找。  
     Author + year -> author lookup.
   - 主题 / 问题 -> 带同义词的概念搜索。  
     Topic / question -> concept search with synonyms.
   - “最新”、“近期”或“今年” -> 对日期敏感的搜索；在文章页面核验发表日期。  
     “Latest”, “recent”, or “this year” -> date-sensitive search; verify publication dates on article pages.
   - 临床或安全问题 -> 证据搜索；优先原始研究加上当前高质量综述，不要把文献检索变成医疗建议。  
     Clinical or safety question -> evidence search; favor primary research plus current high-quality synthesis, and do not turn literature retrieval into medical advice.

3. **按此顺序搜索。** / **Search in this order.**
   1. 官方出版商搜索或期刊档案。  
      Official publisher search or journal archive.
   2. 官方出版商域名上的精确文章页面。  
      Exact article page on the official publisher domain.
   3. 用于发现/交叉核对的结构化元数据源（Crossref；生物医学材料用 PubMed/Europe PMC；可用时用其他索引）。  
      Structured metadata source for discovery/cross-checking (Crossref; PubMed/Europe PMC for biomedical material; other indexes when available).
   4. 若站点搜索不可用或效果差，则限制在官方域名的一般网页搜索。  
      General web search restricted to the official domain if the site search is inaccessible or poor.

4. **生成查询变体。** / **Generate query variants.**
   - 对独特标题或术语使用精确短语。  
     Exact phrase for distinctive titles or terms.
   - 用 2–5 个核心词的短概念查询。  
     Short concept query with 2-5 load-bearing terms.
   - 同义词 / 缩写变体。  
     Synonym / acronym variant.
   - 作者 + 关键词或 DOI 变体。  
     Author + keyword or DOI variant.
   - 仅在广泛搜索返回候选后再添加日期/期刊/文章类型过滤。  
     Add date/journal/article-type filters only after the broad search returns candidates.
   - 详细配方见 `references/query-playbook.md`。  
     See `references/query-playbook.md` for the detailed recipe.

5. **打开并核验候选。** / **Open and verify candidates.**
   切勿仅凭搜索结果摘要就做出实质性主张。打开文章页面并在可用时核验：  
   Never rely on a search-result snippet alone for a substantive claim. Open the article page and verify, when available:
   - 标题 / title
   - 期刊 / 期刊家族 / journal / journal family
   - 文章类型 / article type
   - 作者 / authors
   - 发表日期与在线发表日期 / publication date and online-publication date
   - DOI
   - 与问题相关的摘要 / 概要 / 关键结果 / abstract / summary / key result relevant to the question
   - 更正、撤稿、更新或相关评论状态 / correction, retraction, update, or linked commentary status

6. **只提取有依据的内容。** / **Extract only what is supported.**
   - 将文章元数据与科学主张分开。  
     Separate article metadata from scientific claims.
   - 区分论文自身陈述的结果与你对多篇论文的综合。  
     Distinguish a paper's stated result from your synthesis across papers.
   - 不要从观察性证据推断因果关系。  
     Do not infer causality from observational evidence.
   - 标注付费墙限制或仅摘要级核验。  
     Flag paywall-limited or snippet-only verification.
   - 来源矛盾时报告冲突，并以出版商页面作为文章身份的优先依据。  
     For contradictory sources, report the conflict and prefer the publisher page for article identity.

7. **返回可审计的答案。** / **Return an auditable answer.**
   文献搜索默认用紧凑表格或列表，包含：标题、期刊、日期、DOI/官方链接、文章类型、匹配原因、核验状态。再用散文综合回答。对时间敏感的请求附上搜索日期。  
   For literature searches, default to a compact table or list containing: title, journal, date, DOI/official link, article type, why it matches, and verification status. Then synthesize the answer in prose. Include the search date for time-sensitive requests.

## 期刊路由 / Journal routing

除非请求多刊搜索，否则只加载匹配的适配器：  
Load only the matching adapter unless a multi-journal search is requested:

- Nature / Nature Portfolio -> `references/nature.md`
- Science / AAAS Science journals -> `references/science.md`
- The Lancet / Lancet family -> `references/lancet.md`
- New England Journal of Medicine -> `references/nejm.md`
- JAMA / JAMA Network -> `references/jama.md`
- Cell / Cell Press -> `references/cell.md`
- PNAS / PNAS Nexus -> `references/pnas.md`

跨刊搜索时，加载 `references/source-map.md` 以及所需的期刊适配器。  
For cross-journal searches, load `references/source-map.md` plus the needed journal adapters.

## 访问失败与回退 / Access failures and fallbacks

当直接访问失败、出版商阻止自动化访问、页面需要 JavaScript，或付费墙阻止全文查看时，阅读 `references/network-access.md`。  
Read `references/network-access.md` when direct access fails, the publisher blocks automated access, a page requires JavaScript, or a paywall prevents full-text inspection.

不要绕过身份验证、订阅、验证码、robots 规则或访问控制。改用元数据/摘要来源或可访问的出版商材料。  
Do not bypass authentication, subscriptions, CAPTCHAs, robots rules, or access controls. Use metadata/abstract sources or accessible publisher material instead.

## 可选的确定性搜索助手 / Optional deterministic search helper

在可执行命令且有网络访问时，使用 `scripts/journal_search.py`。它通过期刊特定 ISSN 搜索 Crossref，并输出规范化元数据，适合在出版商页面核验前发现候选。  
Use `scripts/journal_search.py` when command execution and internet access are available. It searches Crossref with journal-specific ISSNs and emits normalized metadata suitable for candidate discovery before publisher-page verification.

示例 / Examples:

```bash
python scripts/journal_search.py --journal nature --query "CRISPR prime editing" --limit 8
python scripts/journal_search.py --journal lancet --query "GLP-1 cardiovascular" --from-date 2025-01-01 --sort published --limit 10
python scripts/journal_search.py --journal science --doi 10.1126/science.ade1499
```

若直接访问 Crossref 失败且本机故意提供了 SOCKS 代理，可添加 `--try-local-socks`。脚本只尝试固定的一小份本地端口列表，永不扫描远程主机。  
If direct Crossref access fails and a local SOCKS proxy is intentionally available, add `--try-local-socks`. The script only tries a small fixed list of localhost ports and never scans remote hosts.

## 质量规则 / Quality rules

- 宁可精确也不要堆量。五篇已核验的论文好过五十篇弱匹配。  
  Prefer precision over volume. Five verified papers are better than fifty weak matches.
- 绝不把姊妹刊标成旗舰刊。  
  Never label a sibling journal as the flagship journal.
- 绝不编造 DOI、期卷、日期、作者、摘要或访问状态。  
  Never fabricate a DOI, issue, volume, date, author, abstract, or access status.
- 标题匹配不等于该论文支持某主张；当支持关系重要时，检查摘要/全文。  
  A title match is not evidence that a paper supports a claim; inspect the abstract/full text when the support relationship matters.
- 对 “最新” 请求，按实际发表/在线发表日期排序，并在出版商网站确认最新候选。  
  For “latest” requests, sort by actual publication/online-publication date and confirm the newest candidates on the publisher site.
- 当结果对用户结论至关重要时，检查更正/撤稿。  
  Check corrections/retractions when the result is central to the user's conclusion.
- 尊重版权：概括而非大段复制文章正文。  
  Respect copyright: summarize rather than reproduce long article text.

## 相关参考 / Related references

- 搜索构建与排序 / Search construction and ranking -> `references/query-playbook.md`
- 网络/代理/付费墙处理 / Network/proxy/paywall handling -> `references/network-access.md`
- 跨出版商来源层级 / Cross-publisher source hierarchy -> `references/source-map.md`
- 设计本包时回顾的公开 Skill 生态 / Public Skill landscape reviewed while designing this package -> `references/existing-skill-review.md`
