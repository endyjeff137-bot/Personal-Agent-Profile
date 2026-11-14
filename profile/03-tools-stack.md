# 03 · 工具与环境

```yaml
---
agent_read: true
kind: fact
priority: normal
updated: 2026-11-14
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
- **全网信息获取：Agent Reach 1.6.1**（2026-11-11 装，MIT 开源，13+ 平台）
  - 已注册为 WorkBuddy skill：`~/.workbuddy/skills/agent-reach/`
  - 可执行文件：`C:\Users\endyj\.local\bin\agent-reach.exe`（已加入用户 PATH）
  - 桌面入口：`全网情报.bat`（诊断/搜索/读链接/加平台/登录）
  - **实测可用**：web 搜索+读网页（Exa+Jina）· B站 搜索/读详情/热榜 · V2EX 全通 · GitHub 走 API
  - **受限**：B站字幕需登录 · YouTube 读取/字幕被 Google 反爬拦 · 小红书需装 Chrome 的 OpenCLI 扩展
  - 能力边界：**只读**，不发帖不评论不点赞；登录一律由用户本人在浏览器完成
  - 抖店用法：竞品视频情报（B站测评/开箱）、选品趋势、竞品价格带、用户吐槽收集

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
- **AI 短剧制片台**（WorkBuddy 专家「短剧导演」`douyin-drama-studio`，2026-11-13 建）
  - 六角色班子：故事编剧 → 副导演 → 场景策划 → 短剧生成 → 剪辑配音 → 影片校对
  - 双击入口：桌面 `短剧制片台.bat`；工作台样例在桌面 `短剧工作台\`
  - 脚本：`~/.workbuddy/plugins/marketplaces/my-experts/plugins/douyin-drama-studio/skills/drama-pipeline/scripts/drama_kit.py`
  - 本地零成本配音：`tts_local.py`（Windows SAPI 中文音色，离线无限量）
  - 成本：60 秒静帧动效版 ~288-480 credits；全 AI 动态 3600 credits（贵 7.5 倍）
  - **关键约束**：商用生图走 agent-earth（FLUX 3 无水印）；WorkBuddy ImageGen 带水印不可商用
  - **角色一致性**：必须用 `reference_image_urls`（H3 Max 支持 9 张），同 seed 不锁脸
  - **v2 真短剧技术栈（2026-11-14 实测）**：MagiHuman 音频驱动口型（24 credits/秒@256p，唯一实测通过的唇动方案）· 可灵 O3 Pro `elements` 命名角色 + `multi_prompt` 一镜多段（135/秒）· CassetteAI 配乐（24/分钟）· FlashVSR 超分（0.6/百万像素）
  - ⚠️ **agent-earth 的 ExecuteTool 必须把 tool_url 放进 params 内部**：`{"params":{"params":{...},"tool_url":"..."}}`，否则间歇性报 "must have required property tool_url"
  - ⚠️ **参考图会锁死面部身份**，提示词改不动 → 每角色必须有独立定妆图
  - **成本预估器**（`cost_estimator.py` + 桌面 `短剧成本预估.bat`）：3 分钟短剧 = 15,286 credits ≈ **¥99**（混合路线标准档）。换算基准：agent-earth 1 USD=1000 credits，汇率 6.7156 → **1 credit ≈ ¥0.0065**
  - ⚠️ **三条计费规则**：①MagiHuman 按【请求时长】计费，与音频长短无关 ②技术性失败不收费（"Failed calls are free"），抽卡只算"成功但质量不达标重做" ③合并台词省不了钱（计费看总秒数不看镜头数）
  - 💡 **256p 生成 + 超分 = 39.7 credits/秒，比 720p 直出（48/秒）便宜 17%**
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
| 2026-11-11 | 新增 Agent Reach 1.6.1 全网信息获取（13+平台，MIT开源）；已注册为 WorkBuddy skill，实测 web/B站/V2EX/GitHub 可用；桌面入口「全网情报.bat」；顺带装了 gh CLI 2.103.3（待登录） |
