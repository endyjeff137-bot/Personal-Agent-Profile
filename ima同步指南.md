# ima 知识库同步指南

> 实测日期：2026-11-23　｜　知识库：徐轩强 Jeff的知识库（`ima_kb_6VlZ6eIh`）

---

## 一、先说结论：网页链接导入**不会**自动更新

我原本以为「把 GitHub 仓库链接丢进 ima，仓库一改 ima 自动跟上」。**实测证明这是错的。**

### 实测过程

1. 往 GitHub 推了一个可识别的标记改动（`<!-- ima-sync-test -->`）
2. 等 90 秒后读 ima 里的内容 → **标记没出现，内容纹丝不动**
3. 对同一 URL 重新 `import_urls` → media_id 不变，**内容仍是旧的**
   （ima 缓存了首次抓取的结果，重复导入不会重抓）

官方资料里那句「导入的文档与源文件保持自动同步」**专指腾讯文档**，网页链接不适用。

### 那什么方案可靠？本地 Markdown 文件上传

实测可用，三步：

```
1) ima MCP create_media       → 拿 media_id + COS 预签名上传地址
2) curl -X PUT 上传文件到 COS → 必须原样带上 auth_headers 的全部 header
3) ima MCP add_knowledge      → duplicate_name_strategy=REPLACE
```

**验证过的两点：**
- 标题是干净的 `AGENT.md`，不是一整条长 URL
- `REPLACE` 按**文件名**匹配，同名条目会被覆盖，**不会产生重复**
  （实测：总条目数不变，file_size 从 2055 → 2160，说明覆盖成功）

---

## 二、两条路线的对比

| | import_urls（网页链接） | 本地文件上传（推荐） |
|---|---|---|
| 内容自动更新 | ❌ 快照，不重抓 | ❌ 同样要手动跑，但可脚本化 |
| 标题 | 整条长 URL，无法辨认 | `AGENT.md` 干净可读 |
| 同名覆盖 | ⚠️ 改名加时间戳（`06-goals_261123164859.md`） | ✅ REPLACE 正确覆盖 |
| 内容质量 | Markdown 被包成 ```` 围栏 | Markdown 正常解析 |
| 更新触发 | 无 | 跑一次脚本 |
| 适用 | 外部网页、公众号文章 | 本仓库档案 |

**结论**：档案这种「本地维护、GitHub 同步」的内容，走本地上传；标题干净、覆盖正确，后续更新跑脚本即可。

---

## 三、同步流程

### 一键检查（本地改完、推 GitHub 之后跑）

```bash
python ima_sync.py --check
```

输出示例：
```
[ima-sync] ⚠ 本地有未提交/未推送的改动：
[ima-sync]    ?? xxx.md
[ima-sync]  先跑 push.bat 推送，否则同步到 ima 的会是旧内容。
[ima-sync] 全部 24 个文件与 GitHub 一致
```

### 生成待上传清单

```bash
python ima_sync.py --manifest
```

产出 `ima_sync_manifest.json`，含每个文件的 `file_path` / `file_size` / `content_type`。

### 实际入库（由 WorkBuddy 通过 ima MCP 执行）

对清单里每个文件，依次：

**Step 1** — 申请上传地址
```
ima MCP create_media
  knowledge_base_id: ima_kb_6VlZ6eIh
  apply_upload_mode: 1
  content_type: text/markdown
  file_ext: md
  file_name: <文件名，如 AGENT.md>
  file_size: <精确字节数>
→ 返回 media_id + upload_url.presigned_url + upload_url.auth_headers
```

**Step 2** — 上传（header 一个都不能少）
```bash
curl -X PUT "<presigned_url>" \
  -H "Content-Length: <file_size>" \
  -H "Content-Type: text/markdown" \
  -H "x-cos-acl: private" \
  --data-binary "@<本地文件路径>"
```
> ⚠️ `Content-Length` 必须与 Step 1 传入的 `file_size` **完全一致**，否则签名校验失败。
> ⚠️ `auth_headers` 里的 header 必须**原样携带**，不能增删。

**Step 3** — 入库（用 REPLACE 覆盖同名条目）
```
ima MCP add_knowledge
  knowledge_base_id: ima_kb_6VlZ6eIh
  media_id: <Step 1 的 media_id>
  duplicate_name_strategy: DUPLICATE_NAME_STRATEGY_REPLACE
```

---

## 四、几个坑

| 坑 | 现象 | 解法 |
|---|---|---|
| **文件名撞车** | 根目录 `README.md` 与 `private/README.md` 同名 | 上传时用 `file_name` 区分，如 `private-README.md` |
| **Content-Length 不符** | 上传返回签名校验失败 | 必须用 Step 1 传入的 `file_size`，不能用 `stat` 后的新值 |
| **漏 header** | 上传失败 | `auth_headers` 里三个 header 全带上 |
| **先推 GitHub 再同步** | ima 里是旧内容 | 顺序固定：改 → `push.bat` → `--check` → 上传 |
| **解析未完成** | 刚上传完搜不到 | 等 30–60 秒，`media_state=2` 且 `parse_progress=100` 才是完成 |
| **不能删除条目** | ima MCP **没有删除接口** | 只能靠同名 REPLACE 覆盖；多余条目需在客户端手动删 |

---

## 五、当前知识库状态（2026-11-23）

- 总条目：**49**
- 本地 Markdown 版本：**24 条**（标题干净，可 REPLACE 覆盖）← **这批是主力**
- 网页链接版本：**24 条**（标题是长 URL，内容是快照，不会更新）
- 原有文档：1 条（ima 官方使用指南）

> 网页链接那批是首次尝试留下的。因为 MCP 无删除接口，无法通过 API 清理。
> **如果不想看到两批重复条目，需要在 ima 客户端手动删掉标题带
> `https://raw.githubusercontent.com/...` 的那 24 条**，保留干净文件名的这批。
> 删掉不影响检索——内容完全相同，只是标题更难看而已。

---

## 六、想彻底自动化？

ima 的「Copilot + Skill 定时任务」可以做，但需要 ima 客户端内配置，
不属于本仓库脚本能覆盖的范围。当前 `ima_sync.py` 已经把「检查差异」和
「生成清单」做好了，剩下的上传三步每次约 2 分钟。
