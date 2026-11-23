#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ima_sync.py —— 把 Personal-Agent-Profile 同步到 ima 知识库

═══ 为什么用「本地文件上传」而不是「import_urls」═══

实测结论（2026-11-23）：
1. **import_urls 是快照，不会自动更新**。
   实测：往 GitHub 推一个标记改动后等 90 秒，ima 里的内容纹丝不动。
   再对同一 URL 重复 import_urls，media_id 不变、内容仍是旧的
   —— ima 缓存了首次抓取的结果，不会重抓。
   （官方资料里"与源文件保持自动同步"专指**腾讯文档**，网页链接不适用。）
2. **import_urls 的标题是整条长 URL**，在 ima 界面里完全没法辨认。
3. **本地 Markdown 上传**：标题是干净的 `06-goals.md`，
   且 `add_knowledge` 带 `DUPLICATE_NAME_STRATEGY_REPLACE` 可覆盖同名条目。

所以：本地文件 → create_media → COS 直传 → add_knowledge(REPLACE) 是可靠路径。

═══ 用法 ═══

  # 同步全部 24 个档案文件
  python ima_sync.py

  # 只同步指定文件
  python ima_sync.py AGENT.md profile/01-preferences.md

  # 只看状态，不上传
  python ima_sync.py --check

═══ 依赖 ═══
本脚本不直接调 ima API（需要 MCP 凭证）。
它做两件事：
  1) 检查本地档案与 GitHub 是否同步
  2) 打印待同步清单 + 每个文件的 media 申请指令
真正的入库由 WorkBuddy 通过 ima MCP 工具执行（见 SKILL 文档）。
"""

import os
import sys
import json
import hashlib
import subprocess
import argparse
import urllib.request
import urllib.error

REPO_DIR = os.path.expanduser(
    r"~\.workbuddy\profiles\Personal-Agent-Profile")
RAW_BASE = ("https://raw.githubusercontent.com/endyjeff137-bot/"
            "Personal-Agent-Profile/main/")

KB_ID = "ima_kb_6VlZ6eIh"

# 需要同步的文件（与已导入的 24 条一一对应）
SYNC_FILES = [
    "AGENT.md", "README.md", "QUICKSTART.md", "GITHUB-AUTH.md",
    "profile/00-identity.md", "profile/01-preferences.md",
    "profile/02-work-context.md", "profile/03-tools-stack.md",
    "profile/04-knowledge-map.md", "profile/05-glossary.md",
    "profile/06-goals.md",
    "rules/10-hard-rules.md", "rules/11-style-rules.md",
    "rules/12-forbidden.md",
    "context/20-current-projects.md", "context/21-people.md",
    "context/22-decisions-log.md",
    "memory/30-long-term-memory.md", "memory/31-lessons-learned.md",
    "memory/CHANGELOG.md",
    "prompts/40-my-prompt-library.md", "prompts/41-agent-bootstrap.md",
    "templates/50-templates.md",
    "private/README.md",
]

MIME = {".md": "text/markdown", ".txt": "text/plain"}


def log(msg):
    print("[ima-sync] %s" % msg, flush=True)


def local_path(rel):
    return os.path.join(REPO_DIR, rel.replace("/", os.sep))


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def remote_md5(rel):
    """取 GitHub 上文件的 md5，用来判断本地是否已推送"""
    try:
        with urllib.request.urlopen(RAW_BASE + rel, timeout=20) as r:
            return hashlib.md5(r.read()).hexdigest()
    except Exception as ex:
        return None


def git_status():
    """本地是否有未推送的改动"""
    try:
        r = subprocess.run(
            ["git", "-C", REPO_DIR, "status", "--porcelain"],
            capture_output=True, text=True, timeout=30)
        return r.stdout.strip()
    except Exception:
        return ""


def check():
    """检查本地 vs GitHub 差异"""
    dirty = git_status()
    if dirty:
        log("⚠ 本地有未提交/未推送的改动：")
        for ln in dirty.splitlines():
            log("   %s" % ln)
        log("  先跑 push.bat 推送，否则同步到 ima 的会是旧内容。")
    else:
        log("本地工作区干净（与 GitHub 一致）")

    diffs = []
    for rel in SYNC_FILES:
        p = local_path(rel)
        if not os.path.exists(p):
            log("  ✗ 本地缺失：%s" % rel)
            continue
        lm, rm = md5(p), remote_md5(rel)
        if lm != rm:
            diffs.append(rel)
            log("  ↻ 不一致：%s" % rel)
    if diffs:
        log("共 %d 个文件与 GitHub 不一致" % len(diffs))
    else:
        log("全部 %d 个文件与 GitHub 一致" % len(SYNC_FILES))
    return diffs


def build_manifest():
    """生成待上传清单（给 WorkBuddy 用 MCP 执行）"""
    manifest = []
    for rel in SYNC_FILES:
        p = local_path(rel)
        if not os.path.exists(p):
            continue
        ext = os.path.splitext(rel)[1].lower()
        manifest.append({
            "rel": rel,
            "file_name": os.path.basename(rel),
            "file_path": p,
            "file_size": os.path.getsize(p),
            "content_type": MIME.get(ext, "text/markdown"),
            "file_ext": ext.lstrip("."),
        })
    out = os.path.join(REPO_DIR, "ima_sync_manifest.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"kb_id": KB_ID, "items": manifest}, f,
                  ensure_ascii=False, indent=2)
    log("清单 → %s（%d 个文件）" % (out, len(manifest)))
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Personal-Agent-Profile → ima 知识库同步")
    ap.add_argument("files", nargs="*", help="只同步指定文件")
    ap.add_argument("--check", action="store_true", help="只检查不生成清单")
    ap.add_argument("--manifest", action="store_true",
                    help="生成待上传清单")
    a = ap.parse_args()

    log("仓库：%s" % REPO_DIR)
    log("知识库：%s" % KB_ID)
    print()

    diffs = check()
    print()

    if a.check:
        return 0

    if a.files:
        global SYNC_FILES
        SYNC_FILES = a.files

    build_manifest()
    print()
    log("下一步：让 WorkBuddy 按 manifest 逐个执行")
    log("  1) ima MCP create_media（拿 media_id + presigned_url）")
    log("  2) curl -X PUT 上传文件到 COS（必须带 auth_headers 全部 header）")
    log("  3) ima MCP add_knowledge（duplicate_name_strategy=REPLACE）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
