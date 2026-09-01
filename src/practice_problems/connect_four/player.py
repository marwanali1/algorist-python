from board import DiscColor


class Player:
    def __init__(self, name: str, color: DiscColor):
        self._name = name
        self._color: DiscColor = color

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> DiscColor:
        return self._color
