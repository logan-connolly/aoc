import pytest

from aoc import io


@pytest.fixture
def year():
    return 2020


@pytest.fixture
def day():
    return 1


@pytest.fixture
def mock_project_root(monkeypatch, tmp_path):
    monkeypatch.setattr(io, "get_project_root", lambda: tmp_path)
    return io.get_project_root()
