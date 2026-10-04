#!/bin/bash
# 用法: ./push.sh "这次改了什么"
cd "$(dirname "$0")" || exit 1
MSG="${1:-学习记录 $(date +%Y-%m-%d)}"
git add .
if git diff --cached --quiet; then
  echo "没有新的改动，不需要提交"
  exit 0
fi
git commit -m "$MSG" && git push && echo "已推送到 GitHub"
