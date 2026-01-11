.PHONY: help install serve build clean

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install dependencies
	bundle install

serve: ## Start the development server (http://localhost:4000)
	bundle exec jekyll serve

serve-livereload: ## Start the development server with live reload
	bundle exec jekyll serve --livereload

build: ## Build the site for production
	bundle exec jekyll build

clean: ## Remove generated site and caches
	bundle exec jekyll clean
