import pytest

from aoc import io


def test_init_module_dir(year, day, mock_project_root):
    io.initialize_module_dir(year, day)
    path_to_module = io.get_path_to_module(year, day)
    assert path_to_module.exists()
    assert (path_to_module / "__init__.py").exists()
    assert (path_to_module / "solver.py").exists()


def test_init_data_dir(year, day, mock_project_root):
    io.initialize_data_dir(year, day)
    path_to_data = io.get_path_to_input_data(year, day)
    assert path_to_data.exists()