RUSTKYLL ?= rustkyll
RUSTKYLL_REV ?= 636818031d70529a3ad6261771d91ce896e1771f
RUSTKYLL_BUILD_FLAGS ?=
RUSTKYLL_SERVE_FLAGS ?=

.PHONY: help install serve build clean

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install dependencies
	cargo install --git https://github.com/alexeygrigorev/rustkyll.git --rev $(RUSTKYLL_REV) --locked rustkyll

serve: ## Start the development server (http://localhost:4000)
	$(RUSTKYLL) serve $(RUSTKYLL_SERVE_FLAGS)

serve-livereload: ## Start the development server with live reload
	$(RUSTKYLL) serve --livereload $(RUSTKYLL_SERVE_FLAGS)

build: ## Build the site for production
	$(RUSTKYLL) build $(RUSTKYLL_BUILD_FLAGS)

clean: ## Remove generated site and caches
	rm -rf _site .rustkyll-manifest.json
