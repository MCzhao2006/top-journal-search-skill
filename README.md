# Top Journal Search

中英双语 / Bilingual (中文 · English)

搜索、定位、核验并综合来自顶尖科学与医学期刊网站的 Agent Skill，专为 **Nature、Science (AAAS)、The Lancet、NEJM、JAMA、Cell、PNAS** 提供专用路由。

An Agent Skill for searching, locating, verifying, and synthesizing information from leading scientific and medical journal websites, with dedicated routing for **Nature, Science (AAAS), The Lancet, NEJM, JAMA, Cell, and PNAS**.

优先使用官方出版商页面作为文章身份与文章级事实的首选来源；书目数据库仅作发现与回退辅助。  
Prefer official publisher pages as the primary source for article identity and article-level facts; use bibliographic databases only as discovery/fallback aids.

---

## 功能 / Features

- 旗舰刊与期刊家族清晰区分  
  Clear distinction between flagship journals and their families
- 按标题 / 作者 / DOI / 主题 / 日期精确定位  
  Exact lookup by title, author, DOI, topic, or date
- Crossref + 出版商页面双重核验  
  Dual verification via Crossref + publisher pages
- 更正、撤稿、更新状态检查  
  Checks for corrections, retractions, and updates
- 网络失败与付费墙的安全回退策略  
  Safe fallback strategies for network failures and paywalls
- 可选本机 SOCKS5 代理（仅 localhost）  
  Optional local SOCKS5 proxy (localhost only)

## 适用场景 / When to Use

当用户或智能体需要：  
When a user or agent needs to:

- 在顶刊网站查找论文  
  Find papers on top-journal websites
- 按标题、作者、DOI、主题或日期定位文章  
  Locate an article by title, author, DOI, topic, or date
- 跨 Nature / Science / Lancet / NEJM / JAMA / Cell / PNAS 比较证据  
  Compare evidence across these journals
- 核验文章元数据或更正状态  
  Verify article metadata or correction status
- 识别近期论文并提取有来源依据的事实  
  Identify recent papers and extract source-grounded facts

## 快速使用 / Quick Start

### 1. 作为 Agent Skill 安装 / Install as Agent Skill

```bash
cp -r top-journal-search /path/to/your/skills/
```

Skill 通过 `SKILL.md` 的 frontmatter 自动触发。  
The skill is automatically triggered via the frontmatter in `SKILL.md`.

### 2. 直接使用辅助脚本 / Use the Helper Script

```bash
# 按期刊 + 主题搜索 / Search by journal + topic
python scripts/journal_search.py --journal nature --query "CRISPR prime editing" --limit 8

# 带日期过滤 / With date filter
python scripts/journal_search.py --journal lancet --query "GLP-1 cardiovascular" --from-date 2025-01-01 --sort published --limit 10

# 按 DOI 精确查找 / Exact DOI lookup
python scripts/journal_search.py --journal science --doi 10.1126/science.ade1499

# 直接访问失败时尝试本机 SOCKS5 / Try local SOCKS5 if direct access fails
python scripts/journal_search.py --journal cell --query "organoid" --try-local-socks
```

依赖：Python 3.8+（标准库）。可选 `curl` 做 SOCKS5 回退。  
Requirements: Python 3.8+ (stdlib only). Optional `curl` for SOCKS5 fallback.

## 支持的期刊 / Supported Journals

| 旗舰刊 / Flagship | 家族 / Family | 适配器 / Adapter |
|-------------------|---------------|------------------|
| Nature | Nature Portfolio | `references/nature.md` |
| Science | AAAS Science journals | `references/science.md` |
| The Lancet | Lancet family | `references/lancet.md` |
| NEJM | — | `references/nejm.md` |
| JAMA | JAMA Network | `references/jama.md` |
| Cell | Cell Press | `references/cell.md` |
| PNAS | PNAS Nexus | `references/pnas.md` |

## 工作流概览 / Workflow Overview

1. 确定范围（旗舰刊 vs 家族）  
   Resolve scope (flagship vs family)
2. 分类查询（精确 / 作者 / 主题 / 最新 / 临床）  
   Classify the lookup
3. 按优先级搜索（出版商 → 文章页 → 元数据索引 → 域名限制网页搜索）  
   Search in priority order
4. 生成查询变体并打开页面核验  
   Generate query variants and verify on article pages
5. 只提取有依据的内容，返回可审计结果  
   Extract only supported content and return auditable results

## 质量原则 / Quality Principles

- 宁可精确也不要堆量  
  Prefer precision over volume
- 绝不把姊妹刊标成旗舰刊  
  Never label a sibling journal as the flagship
- 绝不编造 DOI、日期、作者或摘要  
  Never fabricate DOI, date, author, or abstract
- 标题匹配 ≠ 支持主张；需检查摘要/全文  
  Title match ≠ claim support; inspect abstract/full text
- 对关键结果检查更正与撤稿  
  Check corrections/retractions for critical results
- 尊重版权：概括而非大段复制  
  Respect copyright: summarize, do not reproduce long text

## 文件说明 / File Structure

| 文件 / File | 说明 / Description |
|-------------|--------------------|
| `SKILL.md` | Skill 主指令与触发描述 / Main skill instructions and trigger |
| `references/query-playbook.md` | 查询构建与排序策略 / Query construction and ranking |
| `references/network-access.md` | 网络、代理与付费墙处理 / Network, proxy, and paywall handling |
| `references/source-map.md` | 跨出版商来源层级 / Cross-publisher source hierarchy |
| `references/nature.md` 等 | 各期刊专用适配器 / Journal-specific adapters |
| `scripts/journal_search.py` | Crossref 元数据搜索助手 / Crossref metadata search helper |
| `agents/openai.yaml` | Agent 平台显示元数据 / Display metadata for agent platforms |

## License

MIT License

## 贡献 / Contributing

欢迎提交 Issue 与 PR，改进检索策略、增加期刊支持或修复边界情况。  
Issues and PRs are welcome — improvements to search strategy, additional journal support, or edge-case fixes.
