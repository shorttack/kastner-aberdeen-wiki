# Kastner Aberdeen Wiki — common commands

.PHONY: duckdb verify clean rebuild

duckdb:
	@duckdb db/kastner.duckdb

verify:
	@python scripts/verify.py

semantic-search:
	@python scripts/semantic_search.py "$(Q)"

clean:
	@rm -rf wiki data db build_manifest.json
