import pytest

from aoc import io


@pytest.mark.usefixtures("mock_project_root")
def test_init_module_dir(year, day):
    io.initialize_module_dir(year, day)
    path_to_module = io.get_path_to_module(year, day)
    assert path_to_module.exists()
    assert (path_to_module / "__init__.py").exists()
    assert (path_to_module / "solver.py").exists()


@pytest.mark.usefixtures("mock_project_root")
def test_init_data_dir(year, day):
    io.initialize_data_dir(year, day)
    path_to_data = io.get_path_to_input_data(year, day)
    assert path_to_data.exists()
