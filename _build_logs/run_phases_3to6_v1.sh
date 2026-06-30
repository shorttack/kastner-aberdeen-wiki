#!/bin/zsh
# Phases 3-6 wiki rebuild after L7 access promotion.
# Run in your own Terminal:  zsh ~/Repos/kastner-aberdeen-wiki/_build_logs/run_phases_3to6_v1.sh
# v1 2026-06-28. caffeinate keeps Mac awake; tee logs; chain aborts on any phase failure.
set -u
WIKI=/Users/scott/Repos/kastner-aberdeen-wiki
ARCHIVE=/Users/scott/Desktop/Archive/aberdeen-group-archive
PY=/usr/local/bin/python3
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
LOG=$WIKI/_build_logs/phases_3to6_${STAMP}.log

run() {  # $1=label  $2...=command
  local label=$1; shift
  echo "" | tee -a "$LOG"
  echo "==================== $label  $(date -u +%H:%M:%SZ) ====================" | tee -a "$LOG"
  caffeinate -dimsu "$@" 2>&1 | tee -a "$LOG"
  local rc=${pipestatus[1]}
  if [ $rc -ne 0 ]; then
    echo "!!! $label FAILED rc=$rc — aborting chain." | tee -a "$LOG"
    exit $rc
  fi
  echo ">>> $label OK" | tee -a "$LOG"
}

echo "Logging to: $LOG"
run "PHASE 3 (vault, full tier-1)" $PY $ARCHIVE/scripts/build/03_generate_vault_v2.py --wiki $WIKI --archive $ARCHIVE
run "PHASE 4 (indices)"            $PY $ARCHIVE/scripts/build/04_generate_indices_v2.py --wiki $WIKI
run "PHASE 5 (embeddings)"         $PY $ARCHIVE/scripts/build/05_compute_embeddings_v3.py --wiki $WIKI
run "PHASE 6 (scaffolding)"        $PY $ARCHIVE/scripts/build/06_emit_scaffolding_v1.py --wiki $WIKI

echo "" | tee -a "$LOG"
echo "==================== ALL PHASES 3-6 COMPLETE  $(date -u +%H:%M:%SZ) ====================" | tee -a "$LOG"
echo "Log: $LOG"
