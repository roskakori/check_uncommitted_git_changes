#!/bin/sh
set -e
poetry run pytest --cov=check_uncommitted_git_changes --cov-branch --cov-report=html
echo "🎉 Successfully built test coverage report in htmlcov/index.html"
