.PHONY: update
update: # Update index.html with new data from posts
	scripts/update.py

.PHONY: run
run: # Run locally to port 8080
	scripts/run.sh


