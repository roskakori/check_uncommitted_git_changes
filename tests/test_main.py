# Copyright (c) 2022, Thomas Aglassinger.
# All rights reserved. Distributed under the BSD License.
import pytest

from check_uncommitted_git_changes.main import has_uncommitted_git_changes, main_without_logging_setup, print_git_diffs


def test_can_show_help():
    with pytest.raises(SystemExit):
        main_without_logging_setup(["--help"])


def test_can_show_version():
    with pytest.raises(SystemExit):
        main_without_logging_setup(["--version"])


def test_can_check_for_uncommitted_git_changes():
    assert isinstance(has_uncommitted_git_changes(), bool)


def test_can_print_git_status():
    print_git_diffs()
