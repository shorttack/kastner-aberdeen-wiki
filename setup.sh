#!/usr/bin/env bash
# Mac Mini M4 bootstrap for the Kastner Aberdeen Wiki query environment.
# Idempotent — safe to re-run. See SETUP.md for the full walkthrough.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

# ---------- helpers ----------------------------------------------------------
say()  { printf "\n\033[1;36m==>\033[0m %s\n" "$*"; }
warn() { printf "\n\033[1;33m[warn]\033[0m %s\n" "$*"; }
fail() { printf "\n\033[1;31m[fail]\033[0m %s\n" "$*"; exit 1; }
have() { command -v "$1" >/dev/null 2>&1; }

# ---------- 0. sanity --------------------------------------------------------
say "Detected macOS $(sw_vers -productVersion 2>/dev/null || echo 'unknown')"
[[ "$(uname -s)" == "Darwin" ]] || warn "This script targets macOS. Continuing anyway."
[[ "$(uname -m)" == "arm64"  ]] || warn "Not running on Apple Silicon. The 32b model will be slow."

if ! xcode-select -p >/dev/null 2>&1; then
  say "Installing Xcode Command Line Tools (GUI prompt will appear)"
  xcode-select --install || true
  fail "Re-run ./setup.sh after Xcode CLT install completes."
fi

# ---------- 1. Homebrew ------------------------------------------------------
if have brew; then
  say "Homebrew already installed: $(brew --version | head -1)"
else
  say "Installing Homebrew"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Add brew to PATH for this session (Apple Silicon path)
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# ---------- 2. DuckDB CLI ----------------------------------------------------
if have duckdb; then
  say "DuckDB already installed: $(duckdb --version)"
else
  say "Installing DuckDB CLI"
  brew install duckdb
fi

# ---------- 3. Python 3.11 + venv -------------------------------------------
if have python3.11; then
  say "Python 3.11 already installed: $(python3.11 --version)"
else
  say "Installing Python 3.11"
  brew install python@3.11
fi

if [[ -d "$REPO_ROOT/.venv" ]]; then
  say ".venv already exists; reusing"
else
  say "Creating virtualenv at .venv/"
  python3.11 -m venv "$REPO_ROOT/.venv"
fi

# shellcheck source=/dev/null
source "$REPO_ROOT/.venv/bin/activate"

say "Upgrading pip + installing Python requirements"
python -m pip install --upgrade pip --quiet
python -m pip install --quiet -r requirements.txt

# ---------- 4. Ollama --------------------------------------------------------
if have ollama; then
  say "Ollama already installed: $(ollama --version)"
else
  say "Installing Ollama"
  brew install ollama
fi

# Make sure the daemon is running (idempotent)
if ! pgrep -x ollama >/dev/null 2>&1; then
  say "Starting Ollama daemon in the background"
  nohup ollama serve >/tmp/ollama.log 2>&1 &
  sleep 3
fi

pull_if_missing() {
  local model="$1"
  if ollama list 2>/dev/null | awk 'NR>1 {print $1}' | grep -q "^${model}$"; then
    say "Model already present: ${model}"
  else
    say "Pulling ${model} (this can take several minutes)"
    ollama pull "${model}"
  fi
}

pull_if_missing "qwen3:32b"
pull_if_missing "qwen3:30b-a3b"
pull_if_missing "nomic-embed-text-v2-moe"

# ---------- 5. Install the `kw` helper into the venv -------------------------
say "Installing the 'kw' CLI helper into .venv/bin"
cat > "$REPO_ROOT/.venv/bin/kw" <<'KWEOF'
#!/usr/bin/env bash
# Kastner Wiki helper CLI. See SETUP.md for full reference.
set -euo pipefail
# Resolve repo root: kw lives in <repo>/.venv/bin/kw
SELF="$0"
while [[ -L "$SELF" ]]; do
  SELF="$(readlink "$SELF")"
done
REPO="$(cd "$(dirname "$SELF")/../.." && pwd)"
cd "$REPO"

cmd="${1:-help}"; shift || true

case "$cmd" in
  query)
    [[ $# -ge 1 ]] || { echo "usage: kw query \"<question>\""; exit 1; }
    Q="$*"
    python scripts/semantic_search.py "$Q" --k 8 > /tmp/kw_hits.txt
    echo "--- top retrieved pages ---"
    cat /tmp/kw_hits.txt
    echo
    echo "--- Ollama answer (qwen3:30b-a3b) ---"
    # Concatenate top 3 pages as context
    paths=$(grep -oE 'wiki/[^[:space:]]+\.md' /tmp/kw_hits.txt | head -3)
    ctx=""
    for p in $paths; do
      [[ -f "$p" ]] && ctx="$ctx

# Source: $p
$(cat "$p")"
    done
    printf "Use only the context below to answer.\n\nQuestion: %s\n\nContext:%s\n" "$Q" "$ctx" \
      | ollama run qwen3:30b-a3b
    ;;
  sql)
    duckdb db/kastner.duckdb
    ;;
  page)
    [[ $# -ge 1 ]] || { echo "usage: kw page <slug-or-keyword>"; exit 1; }
    KEY="$1"
    HIT=$(find wiki -type f -iname "*${KEY}*.md" | head -1)
    [[ -n "$HIT" ]] || { echo "no page matched: $KEY"; exit 1; }
    echo "opening $HIT"
    open -a Obsidian "$HIT" 2>/dev/null || open "$HIT"
    ;;
  verify)
    python scripts/verify.py
    ;;
  reembed)
    sub="${1:-help}"
    case "$sub" in
      nomic)  python scripts/reembed.py --ollama nomic-embed-text-v2-moe ;;
      minilm) python scripts/reembed.py --model sentence-transformers/all-MiniLM-L6-v2 ;;
      *) echo "usage: kw reembed {nomic|minilm}"; exit 1 ;;
    esac
    ;;
  help|--help|-h|"")
    cat <<HELP
kw — Kastner Wiki helper

  kw query "<question>"   Semantic search + Ollama RAG (qwen3:30b-a3b)
  kw sql                  Open DuckDB shell on kastner.duckdb
  kw page <slug-keyword>  Open the matching wiki page in Obsidian
  kw verify               Run scripts/verify.py
  kw reembed nomic        Rebuild embeddings.parquet with nomic 768-dim
  kw reembed minilm       Rebuild embeddings.parquet with MiniLM 384-dim
  kw help                 Show this help
HELP
    ;;
  *)
    echo "unknown command: $cmd"
    echo "run 'kw help' for usage"
    exit 1
    ;;
esac
KWEOF
chmod +x "$REPO_ROOT/.venv/bin/kw"
say "Installed kw helper. Run it with: source .venv/bin/activate && kw help"

# ---------- 6. verify --------------------------------------------------------
say "Running scripts/verify.py"
python scripts/verify.py || warn "verify.py reported issues — inspect the output above."

# ---------- 7. optional re-embed --------------------------------------------
echo
read -r -p "Re-embed with nomic-embed-text-v2-moe (768-dim, ~10 min on M4)? [y/N] " ans
case "$ans" in
  y|Y|yes|YES)
    say "Re-embedding via Ollama"
    python scripts/reembed.py --ollama nomic-embed-text-v2-moe
    ;;
  *)
    say "Skipping re-embed. You can run 'kw reembed nomic' later."
    ;;
esac

# ---------- 8. done ----------------------------------------------------------
say "Setup complete."
cat <<EOM

Next steps:
  1. Install Obsidian:  https://obsidian.md/download
     Then open the 'wiki/' subfolder as a vault.
  2. Install Perplexity Desktop:  https://www.perplexity.ai/desktop
  3. Activate the venv whenever you work:
       source .venv/bin/activate
  4. Try it:
       kw query "Did Kastner predict the SaaS shift before 2005?"
       kw sql
       kw page IBM

See SETUP.md for the full reference and troubleshooting.
EOM
