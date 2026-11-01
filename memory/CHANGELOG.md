# CHANGELOG · 档案变更记录

```yaml
---
agent_read: true
kind: index
priority: high
updated: 2026-11-01
confidence: high
---
```

<!-- AGENT-READ:ON -->

> **AI 请优先读这个文件**——它告诉你"最近我变了什么"，比全量重读更快。
> 每次改仓库任何文件，都在这里加一行。**倒序**（新的在最上面）。

## 格式

`[日期] 文件 · 改动类型 · 一句话`

改动类型：`新增` / `修改` / `删除` / `归档`

---

## 2026

- `[2026-11-01] 体检修复 · 修改 · 🔧 消除三处协议/事实不一致：① 体验分口径统一（满分为 5 分制，「480」=千分制换算即 4.8 分，「70」=百分制换算即 0.7 分）② README 的 \`AGENT:KIND=meta\` 改为协议定义的 \`AGENT-BLOCK:START kind=index priority=core\` ③ AGENT.md File Map 补入 README/QUICKSTART/GITHUB-AUTH/push.bat/.gitattributes`
- `[2026-11-01] 30-long-term-memory.md · 修改 · 🧠 填实唯一完全空白的记忆层：10 条核心事实、7 条稳定偏好、6 条反复强调的规则、4 条外部记忆指针`
- `[2026-11-01] 22-decisions-log.md · 修改 · 📝 从真实项目反推补入 5 条决策及理由（固定毛利定价 / 偏远限售 / 阶梯运费换绑 / 优先达人分销 / 档案公开留白）`
- `[2026-11-01] 21-people.md · 修改 · 👥 明确"一人公司故无固定人员"，补 4 条沟通规则；敏感角色统一只留代号层，不写任何个人信息`
- `[2026-11-01] 02-work-context.md · 修改 · ➕ 补客单价约 58 元`
- `[2026-11-01] AGENT.md · 修改 · 🏷️ 填入 GitHub ID endyjeff137-bot，称呼标注为"按对话里的称呼走"，消除两处 \`{{你的称呼}}\` 占位`
- `[2026-10-20] 批量 · 修改 · 🎯 AI 代填核心内容（基于合作观察）：00 身份 / 01 偏好★ / 02 业务背景 / 03 工具 / 04 知识地图 / 05 词典 / 06 目标 / 10 硬规则★ / 11 风格★ / 12 禁区 / 20 当前项目 / 31 教训。完成度 ~85%，🔍 标记为推断项待老板复核`
- `[2026-10-20] 仓库 · 新增 · 🎉 已推送上线：github.com/endyjeff137-bot/Personal-Agent-Profile，27 文件 / 72KB，Public，分支 main，raw 链接已验证可访问`
- `[2026-10-20] GITHUB-AUTH.md · 新增 · 授权指南：浏览器 OAuth / Fine-grained Token / gh CLI 三种方式 + 7 条报错对照表 + 代理开关命令`
- `[2026-10-20] push.bat · 新增 · 一键推送脚本（双击 → 输说明 → 自动 add/commit/push）`

### 2026-10-20

- `[2026-10-20] 全部 · 新增 · 仓库初始化：23 个模板文件，绑定 GitHub 账号 endyjeff137-bot，已本地 git init + 首次 commit`
- `[2026-10-20] QUICKSTART.md · 新增 · 开箱指南：专属链接、一键建仓 URL、push 命令、启动提示词（已填账号）、故障排查表`
- `[2026-10-20] .gitattributes · 新增 · 统一跨平台换行（* text=auto eol=lf），避免 Windows/macOS 混用产生 diff 噪音`
- `[2026-10-20] .gitignore · 修改 · 改为 private/* + !private/README.md，安全提醒文档本身允许上传，其余私有内容仍全部排除`

### {{YYYY-MM-DD}}

- `[2026-11-01] 20-current-projects.md · 修改 · 📌 P4 状态更新为"已完成一轮体检修复"，并补充体验分换算说明`
- `[2026-11-01] 05-glossary.md · 修改 · 📖 体验分条目统一为 5 分制口径`
- `[2026-11-01] 全部 · 新增 · 仓库初始化，创建全部模板文件（未完成填写）`

---

## 更早

（无）

---

## 给 AI 的用法

<!-- AGENT-BLOCK:START kind=rule priority=normal -->
- 如果你**上次已经读过**我的档案，这次只需读本文件**新增的行**，然后按需读对应文件。
- 如果你**第一次读**，读完本文件后按 `AGENT.md` 的文件地图走完整流程。
- 看到 `删除` / `归档` 类型的条目 → 说明某条旧规则**已失效**，不要再用。
<!-- AGENT-BLOCK:END -->
