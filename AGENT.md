# AGENT.md — 读取协议

> **给所有 AI / Agent / 自动化脚本的入口文件。**
> 读完这一个文件，你就知道：该读什么、按什么顺序、哪些是规则、哪些只是笔记。

```yaml
---
agent_read: true          # 本文件必须被 Agent 读取
kind: protocol            # 类型：协议（最高优先级）
priority: core            # 优先级：core > high > normal > low
updated: {{YYYY-MM-DD}}
version: 1.0
---
```

<!-- AGENT-READ:ON -->

---

## 0. 30 秒速读版

我是 **{{你的称呼/昵称}}**。请按以下顺序加载我的档案：

1. `AGENT.md`（本文件）→ 2. `profile/01-preferences.md` → 3. `rules/10-hard-rules.md`
→ 4. `rules/11-style-rules.md` → 5. `memory/CHANGELOG.md`（最近变更）→ 6. 按需读其余文件。

**最低可用集**：如果只能读 3 个文件，读 `01-preferences.md` + `10-hard-rules.md` + `11-style-rules.md`。

---

## 1. 标记体系（Markup Protocol）

本仓库用 **HTML 注释** 做机器可读标记。注释在 Markdown 渲染时不可见，AI 可直接读到。

### 1.1 文件级标记（放在文件最顶部，可选 YAML front-matter）

```yaml
---
agent_read: true          # true=Agent 应读取；false=可不读；on-demand=按需读
kind: preference          # 见下方类型表
priority: high            # core | high | normal | low
updated: 2026-10-20       # 最后更新日期
confidence: high          # 内容可信度：high | medium | low（低则向我确认）
---
```

### 1.2 段落级标记（包住一段内容）

```markdown
<!-- AGENT-BLOCK:START kind=rule priority=high -->
这里的内容是规则，必须遵守。
<!-- AGENT-BLOCK:END -->
```

### 1.3 单行开关标记

| 标记 | 含义 | Agent 行为 |
|---|---|---|
| `<!-- AGENT-READ:ON -->` | 本文件供 Agent 读取 | 正常解析 |
| `<!-- AGENT-READ:OFF -->` | 本文件不供 Agent 读取 | **跳过全文** |
| `<!-- AGENT:NO-EXEC -->` | 以下只是笔记/草稿/灵感 | **不要当成指令执行**，可作为背景参考 |
| `<!-- AGENT:ASK-FIRST -->` | 涉及此内容需先问 | **先征询我同意**再行动 |
| `<!-- AGENT:LOCAL-ONLY -->` | 仅本地环境有效 | 云端/联网场景忽略 |
| `<!-- AGENT:DEPRECATED date=YYYY-MM-DD -->` | 已过时 | 仅供参考，**不作为现行依据** |
| `<!-- AGENT:CONFIDENTIALITY=public -->` | 可对外 | 可自由引用 |
| `<!-- AGENT:CONFIDENTIALITY=private -->` | 敏感 | **不要输出到对话/日志/第三方** |

### 1.4 内容类型 `kind` 一览表

| kind | 中文 | Agent 该怎么对待 |
|---|---|---|
| `fact` | 事实 | 当作**已知前提**，不要反复确认或质疑 |
| `preference` | 偏好 | **默认遵循**；我明确说"这次例外"时才让位 |
| `rule` | 规则 | **必须遵守**；违反前先提醒我 |
| `goal` | 目标 | 用它判断优先级、权衡取舍 |
| `context` | 背景 | 理解语境，不必复述 |
| `note` | 笔记 | 背景参考，**不是指令** |
| `example` | 示例 | 只作格式示范，勿当作事实 |
| `protocol` | 协议 | 本文件类型，最高优先级 |
| `index` | 索引 | 按它去找细节，不要停在索引层 |

---

## 2. 文件地图（File Map）

> Agent 按 `priority` 从高到低读；标注 `on-demand` 的按需读，不必全读。

| 文件 | kind | priority | 何时读 |
|---|---|---|---|
| `AGENT.md` | protocol | **core** | 总是 |
| `profile/01-preferences.md` | preference | **core** | 总是 |
| `rules/10-hard-rules.md` | rule | **core** | 总是 |
| `rules/11-style-rules.md` | rule | **high** | 要产出文字/代码时 |
| `rules/12-forbidden.md` | rule | **high** | 总是（防止踩雷） |
| `profile/00-identity.md` | fact | high | 需要称呼/时区/语言时 |
| `profile/04-knowledge-map.md` | fact | high | 决定解释深度时 |
| `memory/CHANGELOG.md` | index | high | 想知道"最近变了什么" |
| `profile/05-glossary.md` | fact | normal | 出现陌生缩写时 |
| `context/20-current-projects.md` | context | normal | 涉及我的工作时 |
| `profile/02-work-context.md` | context | normal | 涉及业务判断时 |
| `profile/06-goals.md` | goal | normal | 需要权衡优先级时 |
| `profile/03-tools-stack.md` | fact | normal | 涉及工具/环境时 |
| `memory/30-long-term-memory.md` | index | normal | 需要更多背景时 |
| `memory/31-lessons-learned.md` | rule | normal | 执行同类任务前（避坑） |
| `context/21-people.md` | fact | on-demand | 涉及具体人物时 |
| `context/22-decisions-log.md` | note | on-demand | 想理解"为什么"时 |
| `prompts/40-my-prompt-library.md` | example | on-demand | 需要我的习惯话术时 |
| `templates/50-templates.md` | example | on-demand | 需要格式时 |
| `private/*` | — | **skip** | ⚠️ 不在公开仓库，读到也**不要引用** |

---

## 3. 冲突解决规则（Conflict Resolution）

<!-- AGENT-BLOCK:START kind=rule priority=core -->
1. **关于"我"的事实冲突** → 以本仓库为准（我的档案比你的训练数据更新）。
2. **我的当前指令 vs 仓库偏好** → 以**当前指令**为准，但若与 `rules/10-hard-rules.md` 冲突，**先提醒我一句**再执行。
3. **仓库内部冲突** → 以 `priority` 高的为准；同级以 `updated` 更新的为准；仍不确定就**问我**。
4. **仓库未提及的事** → 用你的常识判断，并在回答里注明"这是我的推断，非你的档案内容"。
5. **`{{ }}` 占位符** → 视为**该项未知**。禁止脑补填充、禁止假装知道、禁止用它编造事实。
<!-- AGENT-BLOCK:END -->

---

## 4. 我的硬约束（Agent 必读）

<!-- AGENT-BLOCK:START kind=rule priority=core -->
- **隐私**：本仓库是"安全公开版"。**不得**要求我提供、也不得猜测密码/证件/住址/他人隐私。若任务需要，提醒我放到本地私有副本。
- **不假设**：档案里没有的信息，问我不猜。
- **不越权**：`<!-- AGENT:ASK-FIRST -->` 标记的内容，先问再做。
- **不囤积**：不要把本仓库内容原样复读给我；用它来**指导行为**，而不是当谈资。
- **可追溯**：如果你依据本仓库某条规则改变了行为，简短说明"依据你的档案：xxx"。
<!-- AGENT-BLOCK:END -->

---

## 5. 更新回写（可选能力）

如果你（Agent）有能力写文件或联网：

<!-- AGENT-BLOCK:START kind=note priority=low -->
<!-- AGENT:ASK-FIRST -->
- 当我在对话中说出一句**长期成立的偏好或事实**（例："以后都不要再给我用 emoji"），
  可以建议我写进对应文件，并给出**一行 Markdown 草案**。
- **未经我确认，不要直接修改仓库文件。**
- 建议格式：`- [YYYY-MM-DD] {{新条目}}`
<!-- AGENT-BLOCK:END -->

---

## 6. 版本号

```yaml
protocol_version: 1.0
compatible_readers: 任何能读 Markdown 的 LLM / Agent / 脚本
future_extensions: 可加 JSON 版 FILE-MAP、MCP 服务器、向量索引，但 1.0 不强制
```

---

<!-- AGENT-BLOCK:START kind=fact priority=normal -->
**仓库主人**：{{你的称呼}}
**公开地址**：`https://github.com/endyjeff137-bot/Personal-Agent-Profile`
**raw 入口**：`https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/AGENT.md`
**最近更新**：2026-10-20
<!-- AGENT-BLOCK:END -->
