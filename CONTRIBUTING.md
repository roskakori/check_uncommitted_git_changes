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
