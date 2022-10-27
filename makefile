.PHONY: update
update: # Build python venv with deps
	scripts/update.py

.PHONY: run
run: # Run main script
	scripts/run.sh


