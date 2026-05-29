# scripts/_legacy/

Historical one-shot scripts preserved for forever-archive principle. **Do not run** — these contain hardcoded sandbox paths (`/home/user/workspace/...`) and have been superseded by the production pipeline in `shorttack/aberdeen-group-archive/scripts/build/` (Phase 1 + Phase 2).

Moved here 2026-05-29 as part of WORKLIST §8 (canonical layout migration cleanup). All three last ran 2026-05-26 before the v1.5.0 release.

| Script | Original purpose | Superseded by |
|---|---|---|
| `refresh_data_layer.py` | Pass A v2 propagation — rebuilt parquets + DuckDB from masters | `01_load_csvs_v2.py` + `02_build_data_layer_v3.py` |
| `add_dec_longitudinal_pages.py` | One-time injection of DEC longitudinal study pages | Phase 3 (`03_generate_vault_v2.py`) once masters carry the records |
| `add_pass_a_v2_pages.py` | One-time injection of Pass A v2 study pages | Phase 3 (`03_generate_vault_v2.py`) once masters carry the records |

If you need to re-run the equivalent logic, use the build scripts in the public archive repo with the live wiki path:

```bash
python3 ~/Desktop/Archive/scripts/01_load_csvs_v2.py \
  --archive ~/Desktop/Archive/archive_masters \
  --wiki ~/Repos/kastner-aberdeen-wiki

python3 ~/Desktop/Archive/scripts/02_build_data_layer_v3.py \
  --wiki ~/Repos/kastner-aberdeen-wiki
```
