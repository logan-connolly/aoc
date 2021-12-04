"""This is the Solution for Year 2021 Day 04"""

from copy import deepcopy
from dataclasses import dataclass
from typing import Generator, Optional

from aoc.abstracts.solver import Answers, StrLines


@dataclass
class Position:
    """Details that position on the bingo board"""

    row: int
    column: int


@dataclass
class BingoCell:
    """Data object that holds information of Bingo space"""

    value: int
    activated: bool
    position: Position


class BingoBoard:
    """Defines a Bingo Board with cells with value, activated and position in board"""

    n_rows = 5
    n_cols = 5

    def __init__(self, board_id: int, raw_data: str) -> None:
        """Initialize Board with id and raw data of bingo board numbers"""
        self.board_id = board_id
        self._raw_rows = raw_data.split("\n")
        self.cells = self._generate_bingo_cells()
        self.winner = False

    def __repr__(self):
        """Simple representation of a Bingo Board"""
        return f"BingoBoard(board_id={self.board_id}, winner={self.winner})"

    def _generate_bingo_cells(self) -> dict[int, BingoCell]:
        """Take raw rows and convert to BingoCells use hash map for easy look up"""
        bingo_cells = {}
        for row_idx, row in enumerate(self._raw_rows):
            for column_idx, num in enumerate(row.split()):
                position = Position(row=row_idx, column=column_idx)
                bc = BingoCell(value=int(num), activated=False, position=position)
                bingo_cells[int(num)] = bc
        return bingo_cells

    def activate_cell(self, value: int) -> None:
        """In a given round a value will be drawn, activate cells with said value"""
        if value in self.cells:
            self.cells[value].activated = True

    def check_board(self) -> None:
        """Check if winning conditions are met for board"""
        if len(self.activated) < self.n_rows:
            return None

        valid_row = BoardChecker.check_rows(self)
        valid_column = BoardChecker.check_columns(self)
        self.winner = valid_row | valid_column

    @property
    def activated(self):
        """Get cells that are deacivated on board"""
        return [c for c in self.cells.values() if c.activated]

    @property
    def deactivated(self):
        """Get cells that are deacivated on board"""
        return [c for c in self.cells.values() if not c.activated]


class BoardChecker:
    """Helper class for checking winning conditions of a bingo board"""

    @staticmethod
    def check_rows(board: BingoBoard) -> bool:
        for row_idx in range(board.n_rows):
            check = sum(1 for c in board.activated if c.position.row == row_idx)
            if check == board.n_rows:
                return True
        return False

    @staticmethod
    def check_columns(board: BingoBoard) -> bool:
        for col_idx in range(board.n_cols):
            check = sum(1 for c in board.activated if c.position.column == col_idx)
            if check == board.n_cols:
                return True
        return False


GameSequence = Generator[int, None, None]
BingoBoardMap = dict[int, BingoBoard]


def get_sequence(raw_sequence: str) -> GameSequence:
    """Get game sequence as generator that represents the rounds of bingo game"""
    return (int(num) for num in raw_sequence.split(","))


def get_bingo_boards(raw_boards: list[str]) -> BingoBoardMap:
    """Parse the values of bingo boards and put in hash map to look up by id"""
    return {bid: BingoBoard(bid, data) for bid, data in enumerate(raw_boards)}


def play_round(boards: BingoBoardMap, value: int) -> Optional[BingoBoard]:
    """A round of bingo receives all boards and the value derived from sequence"""
    for board in boards.values():
        board.activate_cell(value)
        board.check_board()
        if board.winner:
            return board
    return None


@dataclass
class WinningBoard:
    board: BingoBoard
    winning_number: int


def play_game(sequence: GameSequence, boards: BingoBoardMap) -> WinningBoard:
    """A game of bingo iterates through a game sequence, ending when winner is found"""
    winning_board = None
    value = 0

    while not winning_board:
        value = next(sequence)
        winning_board = play_round(boards, value)

    return WinningBoard(board=winning_board, winning_number=value)


def calculate_score(winner: WinningBoard) -> int:
    """Calculate bingo score for winner"""
    deactivated_sum = sum(c.value for c in winner.board.deactivated)
    return winner.winning_number * deactivated_sum


def get_last_winner(raw_sequence: str, boards: BingoBoardMap) -> WinningBoard:
    """Find out which board wins last"""

    active_boards = deepcopy(boards)

    while len(active_boards) > 1:
        sequence = get_sequence(raw_sequence)
        winner = play_game(sequence, active_boards)
        del active_boards[winner.board.board_id]

    sequence = get_sequence(raw_sequence)
    return play_game(sequence, active_boards)


class Solver:
    def __init__(self, data: str) -> None:
        self.data = data

    def _preprocess(self) -> StrLines:
        return self.data.split("\n\n")

    def _solve_part_one(self, lines: StrLines) -> int:
        raw_sequence, *raw_boards = lines
        sequence = get_sequence(raw_sequence)
        boards = get_bingo_boards(raw_boards)
        winner = play_game(sequence, boards)
        return calculate_score(winner)

    def _solve_part_two(self, lines: StrLines) -> int:
        raw_sequence, *raw_boards = lines
        boards = get_bingo_boards(raw_boards)
        last_winner = get_last_winner(raw_sequence, boards)
        return calculate_score(last_winner)

    def solve(self) -> Answers:
        lines = self._preprocess()
        ans_one = self._solve_part_one(lines)
        ans_two = self._solve_part_two(lines)
        return Answers(part_one=ans_one, part_two=ans_two)
