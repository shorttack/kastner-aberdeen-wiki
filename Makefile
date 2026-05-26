.PHONY: rebuild phase1 phase2 phase3 phase4 phase5 phase6 verify clean

ARCHIVE ?= ~/Desktop/Archive/aberdeen-group-archive

rebuild: phase1 phase2 phase3 phase4 phase5 phase6 verify

phase1:
	python3 scripts/build/01_load_csvs_v1.py --archive $(ARCHIVE) --wiki .

phase2:
	python3 scripts/build/02_build_data_layer_v1.py --wiki .

phase3:
	python3 scripts/build/03_generate_vault_v1.py --wiki .

phase3-fast:
	python3 scripts/build/03_generate_vault_v1.py --wiki . --skip-llm

phase4:
	python3 scripts/build/04_generate_indices_v1.py --wiki .

phase5:
	python3 scripts/build/05_compute_embeddings_v1.py --wiki .

phase6:
	python3 scripts/build/06_emit_scaffolding_v1.py --wiki .

verify:
	python3 scripts/verify.py --wiki .

clean:
	rm -rf wiki/ data/*.parquet db/ build_manifest.json
