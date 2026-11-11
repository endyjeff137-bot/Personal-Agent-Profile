# 04 · 知识地图（我懂什么 / 不懂什么）

```yaml
---
agent_read: true
kind: fact
priority: high
updated: 2026-11-11
confidence: medium
---
```

<!-- AGENT-READ:ON -->

## ✅ 我已经懂的（一句话带过，别再解释基础）

- 电商基础概念：SKU、GMV、ROI、转化率、客单价、毛利/净利
- 抖音小店后台日常操作（商品发布、运费模板、订单、评价管理）
- 平台规则：体验分、商品卡流量、达人分销 CPS、奖惩中心
- Excel 基础（表格、简单公式）
- 抖音生态的玩法名词（短视频种草、直播、达人带货）

## ❌ 我不懂的（请从零讲，用类比，别甩术语）

- 编程、脚本、命令行（**完全不懂，也无意学**）
- API、Webhook、JSON、Git 原理等技术概念
- 统计学（显著性、样本量、置信区间）
- 服务器、部署、域名、数据库

## 🤔 半懂不懂（最容易出错，请特别确认）

- **ROI 和净利的口径**经常混着用 → 涉及数字时先确认我指的是哪个
- 平台规则细节（限售、违规处置）知道大概但记不全 → 涉及处罚类动作帮我复核

## 📚 抖店官方权威入口（规则会变，以当日公告为准）

| 用途 | 链接 |
|---|---|
| 学习中心 | `https://school.jinritemai.com/doudian/web/home` |
| 新手经营指南 | `https://school.jinritemai.com/doudian/wap?from=buyin_daren&should_full_screen=1` |
| **规则中心** | `https://school.jinritemai.com/doudian/web/rules/nHc6agXtzZR1` |
| **开放平台**（开发者/API） | `https://op.jinritemai.com/` |
| AI 助手说明 | `https://school.jinritemai.com/doudian/web/articlev0/aJBGHwgD3poU` |
| AI 图文发布指南 | `https://school.jinritemai.com/doudian/web/articlev0/aHt5ad18FPgj` |
| 自用型应用入驻指南 | `https://op.jinritemai.com/docs/guide-docs/6/583` |
| 授权介绍 | `https://op.jinritemai.com/docs/guide-docs/133` |

**官方重点关注项**：体验分、价格、资质、虚假交易、发货物流

> ⚠️ **规则会更新**。涉及资质、类目、价格、虚假交易、发货物流的判断，必须查规则中心当日公告，不要凭训练数据里的旧规则回答。

## 🤖 我店铺已开通的官方 AI 功能（2026-11-11 后台实测）

| 功能 | 状态 | 路径 |
|---|---|---|
| AI 助手 | ✅ | 侧边栏固定项 |
| AI 智能成片 | ✅ | `/ffa/content-tool/ai-generate-video-v2` |
| 图文运营 | ✅ | `/ffa/content-tool/ai-generate-figure` |
| **售后小助手** | ✅ | `/ffa/merchant-aftersale-assistant/home` |
| **售后挽单助手** | ✅ | `/ffa/maftersale/aftersale/redeem/assistant` |

> 后两个官方指南里没提，是我店铺已开通但没用起来的。覆盖我客服链路最弱的环节（纠纷仲裁 + 差评挽单）。

## 🔌 官方接入的三条路（我的现状对照）

| 路线 | 我的现状 | 判断 |
|---|---|---|
| ① 抖店内置 AI | ✅ 已开通 5 个（见上表） | 可用但覆盖不了算账/选品/佣金规划 |
| ② 服务市场 | 已有 7 个 MCP 连接器（agent-earth 含蝉妈妈抖音数据、linkfox 1688货源、ai-hive 生图、腾讯文档/会议/邮件） | **不必再买**，缺的是授权不是软件 |
| ③ 开放平台自研 | 🔴 **没有**，全部数据靠 CDP 模拟操作 | ⭐ **真缺口** —— 官方 API = 给现有脚本一张官方通行证，解决风控 + 拿到写权限 |

> ⚠️ 走 ③ 时：账号授权必须在**官方页面由店铺账号本人同意**，绝不把密码/验证码/长期令牌交给非官方页面或个人。
> 建议应用类型选**自用型**（接自己的系统，不是上架服务市场给别人用）。
> 权限申请遵循**最小必要**：先只读（商品/订单/账单/罗盘），稳定后再逐项开写（改价/上架/发货），每项配审批闸门。

**官方五环节经营节奏**（我按这个执行，但**剔除直播**）：

| 环节 | 我的执行方式 |
|---|---|
| 开店准备 | ✅ 已完成，一次性 |
| 选品发品 | `screen_products` 筛货 → `qinghu-douyin-quick-listing` 铺货 → `xzb-dy-move` 管理 |
| 获得流量 | ⚠️ **无直播**：短视频挂车 + 商城商品卡 + 搜索 + 精选联盟达人 + 千川点火器 |
| 订单与售后 | `douyin-service-reply` / `ecom-cs-agent` / 体验分拆解 |
| 每日看数 | `ecom-data-doctor` / `dianshop-compass-analyzer` / `ecommerce-daily-report` |
| 每周复盘 | 见专家包 `references/weekly-review.md`，含"最小可用集 7 问"降级方案 |
| 持续查规则 | 查规则中心当日公告 |

## 学习偏好

<!-- AGENT-BLOCK:START kind=preference priority=normal -->
- 教我新东西：**先给一个能直接照做的例子，再讲原理**（不要反过来）
- 类比来源：**用我行业里的例子**（电商、宠物用品、开店）
- 一次教多少：一次一个概念
- 讲完不用追问我是否理解
- **凡是涉及配置/技术操作的，直接帮我做掉，别教我怎么做**
<!-- AGENT-BLOCK:END -->

## 我常犯的错误（请帮我兜底）

- ⚠️ **算账常忘记算运费和平台扣费** → 任何成本/利润计算，主动帮我核对这两项
- ⚠️ 看到数据就想优化，忽略样本量太小 → 先问一句"这个数据量够下结论吗"
- ⚠️ 容易把"毛利率"和"毛利额"搞混
- ⚠️ 同时开太多事，容易被细节拖住 → 提醒我抓 Top 3

---

## 变更记录

| 日期 | 改了什么 |
|---|---|
| 2026-10-20 | AI 预填 |
