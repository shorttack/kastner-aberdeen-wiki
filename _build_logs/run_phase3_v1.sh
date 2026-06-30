#!/bin/zsh
# Phase 3 full tier-1 wiki regen — launchd-driven, detached from pc bash lifecycle.
# v1 2026-06-28. Writes status sentinels so the agent can poll across sessions.
set -u
WIKI=/Users/scott/Repos/kastner-aberdeen-wiki
ARCHIVE=/Users/scott/Desktop/Archive/aberdeen-group-archive
PY=/usr/local/bin/python3
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
LOGDIR=$WIKI/_build_logs
LOG=$LOGDIR/phase3_launchd_${STAMP}.log
STATUS=$LOGDIR/.phase3_status
echo "$LOG" > $LOGDIR/.phase3_current_log
echo "RUNNING ${STAMP}" > $STATUS
{
  echo "=== Phase 3 launchd run start ${STAMP} ==="
  /usr/bin/caffeinate -dimsu $PY $ARCHIVE/scripts/build/03_generate_vault_v2.py \
    --wiki $WIKI --archive $ARCHIVE
  RC=$?
  echo "=== Phase 3 exit code: $RC ==="
  if [ $RC -eq 0 ]; then echo "DONE $(date -u +%Y%m%dT%H%M%SZ) rc=0" > $STATUS;
  else echo "FAILED $(date -u +%Y%m%dT%H%M%SZ) rc=$RC" > $STATUS; fi
} >> $LOG 2>&1
