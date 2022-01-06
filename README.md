[![PyPI](https://img.shields.io/pypi/v/check_uncommitted_git_changes)](https://pypi.org/project/check_uncommitted_git_changes/)
[![Python Versions](https://img.shields.io/pypi/pyversions/check_uncommitted_git_changes.svg)](https://www.python.org/downloads/)
[![Build Status](https://github.com/roskakori/check_uncommitted_git_changes/actions/workflows/build.yaml/badge.svg)](https://github.com/roskakori/check_uncommitted_git_changes/actions/workflows/build.yaml)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/github/license/roskakori/check_uncommitted_git_changes)](https://opensource.org/licenses/BSD-3-Clause)

# check_uncommitted_git_changes

`check_uncommitted_git_changes` is a command line tool to check for
uncommitted git changes to identify outdated generated content during
continuous integration.

## The problem

While generated code generally should not be committed, there are cases for
where it can make sense, for example `*.po` files containing translations that
are derived from source code.

Developers might change the underlying source code but forget to generate
the files derived from it. This causes headache for the next developer
who wants to a translated message while implementing a separate task, and
not has to deal with the outdated content in some way.

## The solution

If your project uses continuous integration, you can use it to run the
code generators. Ideally they produce the same code that has already been
committed to the repository.

However, if a developer forgot to commit up to date generated code, the
code generators will produce slightly different code that can for example
be viewed using

```bash
git status
```

Calling `check_uncommitted_git_changes` after the generators have run can
check for such changes. If there are none, its exit code is 0 and
continuous integration can continue. If changes are found, the exit code is
1 and continuous integration fails.

## Usage

Add `check_uncommitted_git_changes` to your projects using the respective
command depending on how you manage your Python packages.

For poetry, run:

```bash
poetry add --dev check_uncommitted_git_changes
```

For setuptools, run:

```bash
pip install --upgrade check_uncommitted_git_changes
```

or add an entry to your `*requirements.txt`.

The following example outlines a
[GitHub action](https://github.com/features/actions) step that first collects
all translated messages of a Django project and then checks if they differ
from the versions found in the repository:

```yaml
...
jobs:
  build:
    ...
    steps:
      ...
      - name: Check that translations are up to date
        run: |
          python manage.py makemessages --all --ignore venv --no-location --no-obsolete
          check_uncommitted_git_changes
```

The same principle can be applied to
[other continuous integration platforms](https://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software).

## License

`Check_uncommitted_git_changes` is open source and distributed under the BSD
license. The source code is available from
<https://github.com/roskakori/check_uncommitted_git_changes>.

## Change history

See "CHANGES".

## Development and contributing

For information on how to build the project and contribute to it see "CONTRIBUTING".
