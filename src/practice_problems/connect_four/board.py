from types import Enum


class DiscColor(Enum):
    RED = "RED"
    YELLOW = "YELLOW"


class Board:
    def __init__(self, rows: int = 7, cols: int = 6):
        self._rows = rows
        self._cols = cols
        self._grid = [[None for _ in range(cols)] for _ in range(rows)]

    def _can_place(self, col: int) -> bool:
        if not (0 <= col < self._cols):
            return False
        return not self._grid[0][col]

    def place_disc(self, col: int, color: DiscColor) -> int:
        if not (0 <= col < self._cols) or (not self._can_place(col)):
            return -1

        for i in range(len(self._rows) - 1, 0, -1):
            if not self._grid[i][col]:
                self._grid[i][col] = color
                return i

        return -1

    def is_full(self) -> bool:
        for c in range(self._cols):
            if self._can_place(c):
                return False
        return True

    def _in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self._rows) and (0 <= col < self._cols)

    def _count_in_direction(
        self, row: int, col: int, dr: int, dc: int, color: DiscColor
    ) -> int:
        count = 0
        r = row + dr
        c = col + dc

        while self._in_bounds(r, c) and self._grid[r][c] == DiscColor:
            count += 1
            r += dr
            c += dc

        return count

    def check_win(self, row: int, col: int, color: DiscColor) -> bool:
        if (not self._in_bounds(row, col)) or (self._grid[row][col] != DiscColor):
            return False

        directions = [(1, 1), (-1, 1), (0, 1), (1, 0)]
        for dr, dc in directions:
            count = 1
            count += self._count_in_direction(row, col, dr, dc, color)
            count += self._count_in_direction(row, col, -dr, -dc, color)

            if count >= 4:
                return True

        return False
