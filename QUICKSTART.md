# 🚀 开箱指南 · 专属版

> 账号：**endyjeff137-bot** ｜ 生成时间：2026-10-20 ｜ 状态：✅ 本地文件已备好，待推送到 GitHub

---

## ① 你的专属链接（建好仓库后立即可用）

| 用途 | 链接 |
|---|---|
| 仓库主页 | https://github.com/endyjeff137-bot/Personal-Agent-Profile |
| **AI 入口（最重要）** | https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/AGENT.md |
| 偏好 | https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/profile/01-preferences.md |
| 硬规则 | https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/rules/10-hard-rules.md |
| 输出风格 | https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/rules/11-style-rules.md |
| 变更记录 | https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/memory/CHANGELOG.md |

> ⚠️ 仓库**创建之前**这些链接是 404，属于正常。建完即可访问。

---

## ② 第 1 步：建仓库（点下面的链接，字段已预填）

**👉 https://github.com/new?name=Personal-Agent-Profile&visibility=public&description=%E6%88%91%E7%9A%84%E7%BB%9F%E4%B8%80%20AI%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%BA%95%E5%BA%A7%20%C2%B7%20%E8%B7%A8%E5%B9%B3%E5%8F%B0%E3%80%81%E8%B7%A8%E7%94%B5%E8%84%91%E5%8F%AF%E7%94%A8**

打开后确认：
- Owner = `endyjeff137-bot`
- Repository name = `Personal-Agent-Profile`
- **Public** 已选中
- ⚠️ **不要**勾 "Add a README"、"Add .gitignore"、"Choose a license" —— 本地已经有了，勾了会冲突
- 点 **Create repository**

---

## ③ 第 2 步：把文件推上去（选一条路走）

### 方案 A · 用命令（我已帮你 git init + 首次 commit 好了）

建完仓库后，复制这两行执行（在本机终端 / Git Bash）：

```bash
cd "C:/Users/endyj/WorkBuddy/2026-10-05-10-46-59/Personal-Agent-Profile"
git remote add origin https://github.com/endyjeff137-bot/Personal-Agent-Profile.git
git push -u origin main
```

第一次 push 会弹窗要你登录 GitHub → 用浏览器登录即可（推荐），
或用 **Personal Access Token**（GitHub → Settings → Developer settings → Tokens → repo 权限）。

### 方案 B · 完全不用命令（网页复制粘贴）

1. 打开建好的空仓库页面，点 **Add file → Create new file**
2. 文件名框里**直接粘路径**，GitHub 会自动建文件夹，例如：`profile/01-preferences.md`
3. 把本地对应文件的内容粘进大框
4. 底部 **Commit changes**
5. 23 个文件重复 23 次（约 20–30 分钟，一次性）

> 想省事就走方案 A。以后每次改动也只需要 `git push`。

---

## ④ 第 3 步：填 3 个文件（AI 立刻"认识你"）

按这个顺序，各花 5 分钟：

1. **`profile/01-preferences.md`** ← 最重要，决定 AI 说话的方式
2. **`profile/00-identity.md`** ← 称呼、时区、语言
3. **`rules/11-style-rules.md`** ← 输出格式

填完 push 一次。**其余文件的 `{{ }}` 慢慢补，不填 AI 也能用（会当作"此项未知"）。**

---

## ⑤ 第 4 步：复制这段给任意 AI（已填好你的账号）

```text
请先加载我的个人档案，再开始回答我的问题。

档案地址（按此顺序读取）：
1. https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/AGENT.md
2. https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/profile/01-preferences.md
3. https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/rules/10-hard-rules.md
4. https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/rules/11-style-rules.md
5. https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/memory/CHANGELOG.md

读取要求：
- 严格遵循 AGENT.md 里的标记体系：kind=rule 的内容你必须遵守；kind=note 只是笔记，不要当成指令执行；kind=fact 当作已知前提，不要反复确认。
- 所有 {{ }} 占位符视为"该项未知"，禁止脑补、禁止编造。
- 关于我的事实，以档案为准；我在对话中的当前指令优先于档案偏好，但若违反硬规则请先提醒我。
- 不要复述档案内容给我，用它来指导你的行为。

加载完成后，只用一句话回复："档案已加载，我了解你的基本偏好和规则了。" 然后等我提问。
```

**不同平台怎么塞进去：**

| 平台 | 放哪 |
|---|---|
| ChatGPT | 新对话第一条直接粘；或 Settings → Personalization → Custom Instructions |
| Claude | 新建 Project → Project Knowledge 里粘 / 上传 md 文件 |
| Gemini / 豆包 / DeepSeek | 新对话第一条粘 |
| Cursor | 写进项目根目录 `.cursorrules` 文件 |
| Dify / Coze / n8n | 系统提示词（System Prompt）开头 |
| 本地脚本 / 桌面 Agent | 改读本地路径 `C:\Users\...\Personal-Agent-Profile\AGENT.md` |

**极简版**（AI 不能联网时）：

```text
读取 https://github.com/endyjeff137-bot/Personal-Agent-Profile 这个仓库，
从 AGENT.md 开始，按里面的协议加载我的个人档案，然后只回一句"档案已加载"。
```

---

## ⑥ 第 5 步：换电脑 / 换 AI 时怎么用

- **新电脑**：`git clone https://github.com/endyjeff137-bot/Personal-Agent-Profile.git`
- **已有机子**：改前 `git pull`，改后 `git push`
- **Obsidian**：clone 到 Vault 子目录 + 装 Obsidian Git 插件，自动同步
- **新 AI**：重复第 ⑤ 步，粘贴同一段提示词

---

## ✅ 检查清单

- [ ] GitHub 仓库已建（Public，空仓库）
- [ ] 文件已 push（23 个）
- [ ] 打开 raw 链接能看到 AGENT.md 内容
- [ ] `01-preferences.md` / `00-identity.md` / `11-style-rules.md` 已填
- [ ] 启动提示词已粘给至少一个 AI 并得到"档案已加载"
- [ ] `private/` 里没有放任何真实密码/证件（它不会上传，但也别养成写在本地 md 的习惯）

---

## 🆘 出问题怎么办

| 现象 | 原因 / 解决 |
|---|---|
| raw 链接 404 | 仓库还没建，或分支名是 `master` 不是 `main` → 把链接里 `main` 改成 `master` 试一次 |
| `git push` 提示认证失败 | 用浏览器登录，或去 Settings → Developer settings 生成 Token |
| `git push` 提示 rejected | 网页建仓时勾了 README → 先 `git pull origin main --allow-unrelated-histories` 再 push |
| AI 说打不开链接 | 换用离线极简版（把文件内容直接粘给它） |
