# CHANGELOG · 档案变更记录

```yaml
---
agent_read: true
kind: index
priority: high
updated: {{YYYY-MM-DD}}
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

### 2026-10-20

- `[2026-10-20] 全部 · 新增 · 仓库初始化：23 个模板文件，绑定 GitHub 账号 endyjeff137-bot，已本地 git init + 首次 commit`
- `[2026-10-20] QUICKSTART.md · 新增 · 开箱指南：专属链接、一键建仓 URL、push 命令、启动提示词（已填账号）、故障排查表`
- `[2026-10-20] .gitattributes · 新增 · 统一跨平台换行（* text=auto eol=lf），避免 Windows/macOS 混用产生 diff 噪音`
- `[2026-10-20] .gitignore · 修改 · 改为 private/* + !private/README.md，安全提醒文档本身允许上传，其余私有内容仍全部排除`

### {{YYYY-MM-DD}}

- `[{{YYYY-MM-DD}}] 全部 · 新增 · 仓库初始化，创建全部模板文件（未完成填写）`

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
