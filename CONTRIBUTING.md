# Contributing to check_uncommitted_git_changes

## Getting started

To obtains the source code, run:

```bash
git clone https://github.com/roskakori/check_uncommitted_git_changes.git
cd check_uncommitted_git_changes
```

To work with the project you need a reasonably modern Python 3 and
[poetry](https://python-poetry.org/).

To build the project:

```bash
poetry build
```

To run the tests:

```bash
poetry run pytest
```

To build a test coverage report, run:

```bash
sh scripts/build_test_coverage_report.sh
```

and then open the file `htmlcov/index.html` in your browser.

## Keeping dependencies up to date

To check for new versions of dependencies and update them accordingly, run:

```bash
sh scripts/update_dependencies.sh
```

However, this only updates minor versions and patches. To update to newer
major versions you have to manually check the homepage of the respective
package.

## Checking the coding style

The projects use [pre-commit](https://pre-commit.com/) hooks to check for
various coding guidelines.

To set up pre-commit for the first time (this might run for a while):

```bash
poetry run pre-commit install --install-hooks
```

To manually check the coding style:

```bash
poetry run pre-commit run --all-files
```

## Release cheatsheet

The following notes are only relevant for developers with access to the 
PyPI project.

To add a new release, first update the `pyproject.toml`:
```toml
[tool.poetry]
version = "1.x.x"
```
Next build the project and run the tests to ensure everything works:
```bash
poetry build
poetry run pytest
```
Then create a tag in the repository:
```bash
git tag -a -m "Tagged version 1.x.x." v1.x.x
git push --tags
```
And finally publish the new version on PyPI:
```bash
poetry publish
```
