"""This is the Solution for Year 2021 Day 11"""

from collections import defaultdict
from copy import deepcopy

from aoc.abstracts.solver import Answers, StrLines

OctopusMap = dict[tuple[int, int], int]
AdjacentIndexes = list[tuple[int, int]]
SimulationStep = tuple[OctopusMap, int]


def build_octopus_map(lines: StrLines) -> OctopusMap:
    """Iterate over octopuses and insert them into mapping based on index in grid"""
    mapping = defaultdict(int)
    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            mapping[(row_idx, col_idx)] = int(col)
    return mapping


def increment_energy_level(octopus_map: OctopusMap) -> OctopusMap:
    """Increment each octopus by one energy level"""
    return {idx: energy_level + 1 for idx, energy_level in octopus_map.items()}


def get_adjacents(row: int, col: int) -> AdjacentIndexes:
    """Get sorrounding octopus indexes if exists in grid"""
    above = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
    below = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    beside = [(row, col - 1), (row, col + 1)]
    adjacents = [*above, *below, *beside]
    return [(row, col) for row, col in adjacents if 0 <= row <= 9 and 0 <= col <= 9]


def increment_flashes(octopus_map: OctopusMap) -> SimulationStep:
    """Increment flashes and append newly flashed if flash causes another flash"""
    om = deepcopy(octopus_map)
    flashable_octopuses = {idx for idx, val in om.items() if val > 9}
    flash_count = 0

    while flashable_octopuses:
        current_flashable_octopuses = deepcopy(flashable_octopuses)
        for row, col in current_flashable_octopuses:
            om[(row, col)] = 0
            flash_count += 1
            adjacents = get_adjacents(row, col)
            if adjacents:
                for idx in adjacents:
                    om[idx] += 1 if om[idx] != 0 else 0
                    if om[idx] > 9:
                        flashable_octopuses.add(idx)
            flashable_octopuses.discard((row, col))

    return om, flash_count


def simulate_step(octopus_map: OctopusMap) -> SimulationStep:
    """Perform a simulation step on octopus map returning updated map and flash count"""
    om = deepcopy(octopus_map)
    incremented = increment_energy_level(om)
    return increment_flashes(incremented)


def run_simulations(octopus_map: OctopusMap, steps: int) -> int:
    """Get flash count for a give number of steps"""
    om = deepcopy(octopus_map)
    total_flash_count = 0
    for _ in range(steps):
        om, flash_count = simulate_step(om)
        total_flash_count += flash_count
    return total_flash_count


def is_simultaneous_flash(octopus_map: OctopusMap) -> bool:
    """For a given octopus map check if all energy levels are set to zero"""
    return all(energy_value == 0 for energy_value in octopus_map.values())


def step_until_simultaneous_flash(octopus_map: OctopusMap) -> int:
    """Keep simulating steps until all octopuses flash simultaneously"""
    om = deepcopy(octopus_map)
    step = 0
    while not is_simultaneous_flash(om):
        step += 1
        om, _ = simulate_step(om)
    return step


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.splitlines()

    def _solve_part_one(self, lines: StrLines) -> int:
        octopus_map = build_octopus_map(lines)
        return run_simulations(octopus_map, steps=100)

    def _solve_part_two(self, lines: StrLines) -> int:
        octopus_map = build_octopus_map(lines)
        return step_until_simultaneous_flash(octopus_map)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
