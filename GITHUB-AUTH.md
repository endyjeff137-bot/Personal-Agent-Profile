# 🔑 GitHub 登录授权指南（专属 endyjeff137-bot）

> 生成时间：2026-10-20 ｜ 你的机器：**已装 Git Credential Manager**，走**方式 A** 最省事。
> 已帮你配好：remote = `https://github.com/endyjeff137-bot/Personal-Agent-Profile.git`，用户身份 = `endyjeff137-bot`。

---

## 前提：仓库要先建出来

授权是"允许 push"，但仓库本身得先存在。**先做这步**：

👉 打开（字段已预填）：
`https://github.com/new?name=Personal-Agent-Profile&visibility=public&description=我的统一AI上下文底座`

- Owner：`endyjeff137-bot`
- 选 **Public**
- ⚠️ **不要勾** Add a README / Add .gitignore / Choose a license
- 点 **Create repository**

建完你会看到一个"Quick setup"页面。**保持这个页面开着**，下面要用。

---

## 方式 A · 浏览器登录（推荐，30 秒）

**你什么都不用准备，直接 push 就会弹登录。**

在本机终端（PowerShell 或 Git Bash）执行：

```bash
cd "C:/Users/endyj/WorkBuddy/2026-10-05-10-46-59/Personal-Agent-Profile"
git push -u origin main
```

然后会依次发生：

1. 弹出一个窗口（**Git Credential Manager**），问你用什么方式登录
   → 选 **"Sign in with your browser"**（用浏览器登录）
2. 浏览器自动打开 GitHub 授权页
   → 如果没登录 GitHub，先输账号密码登录
   → 如果已登录，直接看到 **Authorize GitCredentialManager** 按钮
3. 点绿色的 **Authorize**（如果让你输设备码，窗口上会显示一串字母如 `ABCD-1234`，照抄进网页）
4. 浏览器显示 "Success" → 回到终端，push 自动继续
5. 终端刷出一堆 `Writing objects...` 就成功了

**✅ 验证**：打开 https://github.com/endyjeff137-bot/Personal-Agent-Profile ，能看到 25 个文件。

> **一次登录，永久有效**——凭据存在 Windows 凭据管理器里，以后 push 不再问。

---

## 方式 B · Personal Access Token（方式 A 卡住时用）

### 第 1 步：生成 Token

打开（直达链接）：
`https://github.com/settings/personal-access-tokens/new`

或手动：GitHub 右上角头像 → **Settings** → 左侧最下方 **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**

填这些：

| 字段 | 填什么 |
|---|---|
| Token name | `Personal-Agent-Profile` |
| Expiration | 选 **90 days**（安全）；嫌麻烦选 **No expiration** |
| Description | 可选，随便写 |
| Repository access | 选 **Only select repositories** → 下拉选 `Personal-Agent-Profile` |
| Permissions | 点 **Repository permissions** → 找到 **Contents** → 改成 **Read and write** |

拉到最底 → **Generate token**

### 第 2 步：复制 Token

页面显示一串 `github_pat_11A...`（以 `github_pat_` 开头）。
**立刻复制**——关掉页面就再也看不到了。

### 第 3 步：用它 push

```bash
cd "C:/Users/endyj/WorkBuddy/2026-10-05-10-46-59/Personal-Agent-Profile"
git push -u origin main
```

弹窗时：
- Username → 填 `endyjeff137-bot`
- Password → **粘贴那串 token**（不是你的 GitHub 密码！）

> ⚠️ 如果浏览器弹窗抢着让你登网页，想改用 token：
> 先执行 `git credential-manager github logout`，再 push 就会改用命令行问你要用户名密码。

---

## 方式 C · 安装 GitHub CLI（以后想省事可选）

一行安装（已装 winget 的 Windows）：

```powershell
winget install --id GitHub.cli
```

装完重启终端，执行：

```bash
gh auth login
```

按提示选：GitHub.com → HTTPS → **Login with a web browser** → 抄设备码 → 浏览器点授权。
之后 Git 会自动复用这个登录态，`git push` 再也不问。

---

## 🆘 故障排查

| 报错 / 现象 | 原因 | 怎么办 |
|---|---|---|
| `repository not found` | 仓库还没建，或名字打错 | 先按上面"前提"建仓库；确认名字是 `Personal-Agent-Profile` |
| `Permission denied (publickey)` | 用了 SSH 地址 | 执行 `git remote set-url origin https://github.com/endyjeff137-bot/Personal-Agent-Profile.git` |
| `Authentication failed` | 用了 GitHub 密码当密码 | GitHub 从 2021 年起不接受密码，必须用 Token 或浏览器登录（方式 A/B） |
| `fatal: refusing to merge unrelated histories` | 建仓时勾了 README | 先 `git pull origin main --allow-unrelated-histories` 再 push |
| 弹窗一闪而过 / 没弹窗 | GCM 被禁用 | 执行 `git config --global credential.helper manager` 再重试 |
| 卡住不动 / `Failed to connect` | 网络慢（你这台机直连 GitHub 约 11 秒） | 见下方"加速" |
| `src refspec main does not match` | 本地分支不是 main | 执行 `git branch -M main` |

### 加速：走你的闪连代理

你这台机有闪连 VPN（系统代理 `127.0.0.1:19828`）。Git 默认不读系统代理，push 卡住时可临时让它走代理：

```bash
git config --global http.proxy http://127.0.0.1:19828
git config --global https.proxy http://127.0.0.1:19828
```

push 完想取消：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

> 实测：你这台机**直连** github.com 返回 200（约 11.6 秒），通常够用。只有超时才需要设代理。

---

## ✅ 成功后下一步

1. 打开 https://raw.githubusercontent.com/endyjeff137-bot/Personal-Agent-Profile/main/AGENT.md
   → 能看到内容就说明 raw 链接通了
2. 把 `QUICKSTART.md` 第 ⑤ 步那段提示词粘给任意 AI
3. 日常改动：**双击仓库里的 `push.bat`** → 输入一句话说明 → 自动推送

---

## 安全提醒

- Token 等同于密码，**不要贴进任何 md 文件、不要发给我、不要提交到仓库**
- 用完的 Token 可以在 GitHub 设置页随时 Revoke
- 授权时看清是哪个应用在请求（正常是 **Git Credential Manager**）
