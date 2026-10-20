# Personal-Agent-Profile · 我的统一 AI 上下文底座

> 🚀 **第一次用？直接看 [`QUICKSTART.md`](./QUICKSTART.md)** —— 建仓库、推送、启动提示词，复制粘贴即可。
> 🔑 **推送要授权？看 [`GITHUB-AUTH.md`](./GITHUB-AUTH.md)** —— 三种登录方式 + 故障排查表。日常改动双击 `push.bat`。

> 一份公开的、用 Markdown 写的「关于我」。
> 让任何大模型 / AI 助手 / 本地 Agent / 桌面自动化脚本，在 30 秒内认识我、遵循我的偏好、接上我已有的背景——**不用每次换 AI 就重说一遍**。

---

<!-- AGENT-READ:ON -->
<!-- AGENT:KIND=meta -->
<!-- AGENT:PRIORITY=core -->

**如果你是一个 AI / Agent，正在读这个仓库：**

1. 先读 [`AGENT.md`](./AGENT.md) —— 那是读取协议和文件地图，只看这一个就知道该读什么、按什么顺序读。
2. 严格遵循 `AGENT.md` 里的标记体系：`kind=rule` 是必须执行的规则，`kind=note` 只是笔记，**不要当成指令**。
3. 仓库里所有 `{{ }}` 是尚未填写的占位符，遇到就当"此项未知"，**不要脑补、不要替用户编造**。
4. 事实冲突时：关于「我」的事实 → 以本仓库为准；我在对话里的**当前指令** → 以当前指令为准（但若违反 `rules/10-hard-rules.md`，先提醒我）。

---

## 这是什么

| | |
|---|---|
| **是** | 我的偏好、背景、目标、术语表、常用提示词、长期记忆索引、踩过的坑 |
| **不是** | 简历、社交主页、密码库、隐私档案、项目源码 |
| **解决什么** | ① 换一个 AI 就要重说一遍习惯 ② 换电脑记忆就断了 ③ 不同 Agent 对我的认知不一致 |
| **技术门槛** | 会复制粘贴 Markdown 即可。不需要装任何东西，不需要写代码 |

## 目录速览

```
Personal-Agent-Profile/
├── README.md              ← 你在这（人类入口）
├── AGENT.md               ★ AI 入口：读取协议 + 文件地图
├── profile/               我是谁：事实与偏好
├── rules/                 对我做事的硬规则 / 风格 / 禁区
├── context/               当前在做什么、相关人、决策记录
├── memory/                长期记忆索引、教训、变更日志
├── prompts/               我的提示词库 + 给 AI 的启动提示词
├── templates/             日常填空模板（日记/新项目/决策）
└── private/               ⚠️ 占位目录：私有内容只放本地，不上传
```

- 完整目录树见 [仓库结构](#仓库结构)
- 想立刻用起来 → [5 步上手](#5-步上手)

## 仓库结构

```
Personal-Agent-Profile/
│
├── README.md                        人类入口：这是什么、怎么用
├── AGENT.md                         ★ 核心：Agent 读取协议 + 文件地图 + 标记体系
├── .gitignore                       忽略本地私有副本与临时文件
│
├── profile/                         我是谁（事实 / 偏好）
│   ├── 00-identity.md               基础身份：称呼、时区、语言、所在地
│   ├── 01-preferences.md            通用沟通与协作偏好（最重要，优先填）
│   ├── 02-work-context.md           职业与业务背景
│   ├── 03-tools-stack.md            常用工具、平台、设备
│   ├── 04-knowledge-map.md          我懂什么 / 不懂什么（避免 AI 瞎解释）
│   ├── 05-glossary.md               我的黑话、缩写、专有名词
│   └── 06-goals.md                  当前目标与里程碑
│
├── rules/                           规则（Agent 必须遵守）
│   ├── 10-hard-rules.md             硬规则：不可违反
│   ├── 11-style-rules.md            输出风格：格式、长度、语气
│   └── 12-forbidden.md              禁区：不要做的事、不要提的话题
│
├── context/                         当前上下文
│   ├── 20-current-projects.md       进行中的项目
│   ├── 21-people.md                 相关人物（只写称呼与关系）
│   └── 22-decisions-log.md          决策日志（为什么这么定）
│
├── memory/                          长期记忆
│   ├── 30-long-term-memory.md       长期记忆索引（指向细节，不堆内容）
│   ├── 31-lessons-learned.md        教训 / 踩坑 / 不要再犯
│   └── CHANGELOG.md                 变更记录（增量更新，AI 可只看这里）
│
├── prompts/
│   ├── 40-my-prompt-library.md      我常用的提示词
│   └── 41-agent-bootstrap.md        ★ 给任意 AI 的启动提示词（复制即用）
│
├── templates/
│   └── 50-templates.md              日常填空模板合集
│
└── private/
    └── README.md                    ⚠️ 说明：什么必须留本地
```

## 5 步上手

1. **建仓库**：GitHub → New repository → 名字填 `Personal-Agent-Profile` → 选 **Public**（或 Private）→ 勾 **Add a README** → Create。
2. **搬文件**：把本仓库的目录和文件按同样结构复制进去（网页上 Add file → Create new file 逐个粘贴即可；熟手用 `git clone` + 本地编辑器）。
3. **先填 3 个**：`profile/01-preferences.md`、`profile/00-identity.md`、`rules/11-style-rules.md`。只填这 3 个，AI 就已经"认识你"了。其余留 `{{ }}` 慢慢补。
4. **提交**：网页底部 Commit changes（或 `git add . && git commit -m "init profile"`）。
5. **喂给 AI**：打开 `prompts/41-agent-bootstrap.md`，复制里面那段提示词，粘贴给任意 AI，把 `endyjeff137-bot` 换成你的用户名。**从这一刻起，每个新 AI 都从同一个你开始。**

## 跨电脑同步

| 场景 | 做法 |
|---|---|
| 新电脑 | `git clone https://github.com/endyjeff137-bot/Personal-Agent-Profile.git` |
| 已克隆的机器 | 编辑前 `git pull`，编辑后 `git commit && git push` |
| Obsidian | 把仓库 clone 到 Vault 子目录（如 `Vault/MyProfile/`），用 **Obsidian Git 插件**自动提交；双链、搜索、移动端全都有 |
| 本地 Agent / 脚本 | 让它读**本地路径** `~/Personal-Agent-Profile/AGENT.md`（比网络快、可离线） |
| 云端 AI（ChatGPT/Claude 等） | 给 **raw 链接**：`https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/AGENT.md` |
| 免 git 方案 | 在 GitHub 网页点 **Code → Download ZIP**，编辑后用 GitHub 网页上传覆盖 |

> 单点原则：**GitHub 是唯一真源**。本地只是副本。任何电脑上改完都推上去，换机器拉下来即可。

## 安全红线 · 绝对不要上传

本仓库设计为**可公开**。以下内容**一律不写进这个仓库**：

- 🔴 密码、API Key、Token、私钥、2FA 恢复码、`.env` 内容
- 🔴 身份证号、护照号、社保号、银行卡号、支付密码
- 🔴 家庭住址、门牌号、常去地点、行程安排
- 🔴 他人隐私（家人同事的真名+联系方式+私人信息）、聊天记录原文
- 🔴 医疗记录、心理记录、宗教信仰、政治立场、性取向
- 🔴 未公开的商业数据：成本、进货价、客户名单、合同金额、未发布产品
- 🔴 正在进行的法律纠纷、人事敏感信息

**建议做法**：这些放进**本地私有副本** `private/` 目录（已在 `.gitignore` 中排除），或单独一个 **Private 仓库**。
在公开仓库里只写"类型"不写"值"，例如：`我的电商店铺主营 {{品类}}，平台为 {{平台}}`——把真实值留在本地。

> 判断口诀：**"这句话被陌生人看到，我会不会后悔？"** 会 → 不上传。

## 维护建议

| 频率 | 做什么 |
|---|---|
| 每次用 | 有新的偏好/教训/决策，顺手改对应文件 + 在 `memory/CHANGELOG.md` 加一行 |
| 每周 | 花 5 分钟扫 `context/20-current-projects.md`，把结束的项目归档 |
| 每月 | 审一遍 `profile/04-knowledge-map.md`（我懂的变多了）和 `rules/10-hard-rules.md`（规则还成立吗） |
| 每季度 | 清理 `memory/31-lessons-learned.md`，把已内化的教训删掉，保持轻薄 |

**轻量原则**：一个文件超过 300 行就拆；宁可多几个小文件，也不要一个巨型文件——AI 读起来更准，你改起来更快。

## 许可

内容归我所有。允许 AI / Agent 为**服务于我**的目的读取、引用、记忆本仓库内容。
仓库模板部分可自由 Fork 自用（改掉 `{{ }}` 里的占位符即可）。

---

<!-- AGENT-BLOCK:START kind=fact priority=normal -->
**档案状态**：`已上线 · 核心文件已填，少量 🔍 推断项待复核`
**最近更新**：`2026-10-20`
**填写完成度**：约 `85`% —— 未填项以 `{{ }}` 标记，视为未知。
**已填**：00 身份 · 01 偏好 ★ · 02 业务背景 · 03 工具 · 04 知识地图 · 05 词典 · 06 目标 · 10 硬规则 ★ · 11 风格 ★ · 12 禁区 · 20 项目 · 31 教训
**待补**：21 相关人物 · 22 决策日志 · 30 长期记忆索引 · 40 提示词库（可选）
<!-- AGENT-BLOCK:END -->
