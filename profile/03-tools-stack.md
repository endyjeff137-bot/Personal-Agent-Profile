# 03 · 工具与环境

```yaml
---
agent_read: true
kind: fact
priority: normal
updated: 2026-11-03
confidence: medium
---
```

<!-- AGENT-READ:ON -->

> 只写工具名，不写账号/密码/Key。

## 电脑与系统

- 主力电脑：**Windows**（主要工作机）
- 手机：**iPhone**
- 多台电脑：**是（两台）** —— 跨电脑靠 GitHub 同步，档案仓库 clone 即可

## 日常软件

- 笔记/知识库：**无 Obsidian**（2026-11-01 实测未安装）。档案仓库用 VS Code / 记事本 + Git 直接编辑
- 办公：Excel / WPS
- 浏览器：**Chrome**
- 通讯：微信
- 设计/剪辑：**剪映**（2026-11-01 实测已安装，路径 `AppData\Local/JianyingPro`）
- 网络：**闪连 VPN**（系统代理 127.0.0.1:19828，日常工作需要，别当风险项处理）

## AI 工具（我在用）

- 主力 AI 工作台：**WorkBuddy**（带浏览器自动化、定时任务、资料库）
- 桌面 AI Agent：**AutoClaw**（智谱出品，一键安装的本地 OpenClaw 应用，50+ 预装 skill，可接飞书等 IM）
- 其他对话 AI：**豆包、腾讯元宝**（2026-11-01 实测本机已装客户端）
- 编程 AI：不直接使用（交给 WorkBuddy 代做）
- 自动化：WorkBuddy 定时排程 + 本地脚本
- 本地模型：无

## 我自建的专属工具

<!-- AGENT-BLOCK:START kind=fact priority=high -->
- **抖店算账器**（`doudian-roi-calc` skill）：按我的实际成本结构算保本 ROI、可承受获客成本、达人CPS 佣金上限
  - 双击入口：桌面 `抖店算账.bat`
  - 脚本：`~/.workbuddy/skills/doudian-roi-calc/scripts/roi_calculator.py`
  - 纯标准库零依赖，Python 3.8+
  - **用途**：任何涉及投流、定价、运费、佣金、每单件数的算账，先跑它再回答
  - 已用它纠正了旧档案里"ROI < 4"的错误（实际保本 ROI 随运费和件数在 6.4~116 浮动）
- **抖店定价计算器**（`doudian-pricing-calc` skill）：套进货价算合理卖价、最高可接受进货价、达人佣金空间
  - 双击入口：桌面 `抖店定价.bat`
  - 脚本：`~/.workbuddy/skills/doudian-pricing-calc/scripts/pricing_calculator.py`
  - 纯标准库零依赖，Python 3.8+
  - **用途**：新定价、谈供应商、比价带、判断哪款能做达人分销
  - 配套公式：`售价 ≥ 进货价 + (平台扣+运费)÷件数 + 目标单件净利`；做达人分销时分子再乘 `(1−佣金率)`
<!-- AGENT-BLOCK:END -->

## 我愿意接受的技术门槛

<!-- AGENT-BLOCK:START kind=preference priority=high -->
- **只接受复制粘贴和双击运行**，别让我装环境、配依赖
- 命令行：**完全不熟** → 要给我可直接执行的完整命令，或者做成 `.bat` 让我双击
- Git：**会 clone/pull/push 基础命令**，复杂的让 AI 做或写进脚本
- 推荐新工具：**优先用我已有的**；要推新的必须给完整上手步骤
- 需要长期重复做的事 → **给我一个脚本**，别每次让我敲命令
<!-- AGENT-BLOCK:END -->

## 常用平台与后台

- 抖店后台 `fxg.jinritemai.com`
- 巨量千川 `uni-prom`
- 精选联盟 `buyin.jinritemai.com`
- 飞鸽客服 `im.jinritemai.com`
- GitHub（个人档案仓库 `endyjeff137-bot/Personal-Agent-Profile`）

## 我不用的工具（别推荐）

- **Obsidian** —— 未安装，别推荐（除非我明确说要装）
- 编程 IDE / 命令行工作流 —— 我不写代码，交给 AI

---

## 变更记录

| 日期 | 改了什么 |
|---|---|
| 2026-10-20 | AI 预填，含 🔍 推断项 |
| 2026-11-01 | 实测本机核实：剪映已装、Obsidian 未装、AutoClaw 已装、豆包+元宝已装；补剪映路径 |
