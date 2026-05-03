RUSTKYLL ?= ../rustkyl/target/debug/rustkyll

.PHONY: help install serve serve-livereload build clean

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Build local Rustkyll from ../rustkyl
	cd ../rustkyl && cargo build

serve: ## Start the development server (http://localhost:4000)
	$(RUSTKYLL) serve --source . --port 4000 --no-browser --no-livereload

serve-livereload: ## Start the development server with live reload
	$(RUSTKYLL) serve --source . --port 4000 --no-browser --livereload

build: ## Build the site for production
	$(RUSTKYLL) build --source . --destination _site --force

clean: ## Remove generated site and caches
	rm -rf _site .sass-cache
