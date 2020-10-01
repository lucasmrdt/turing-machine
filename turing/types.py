from enum import Enum


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    NOT_MOVE = 'not move'

    def __str__(self) -> str:
        return self.value


class Operation(Enum):
    WRITE = 0
    READ = 1


class SymbolValue(str):
    pass


class StateValue(str):
    pass


class Symbol(SymbolValue):
    NEUTRAL = SymbolValue(' ')


class State(StateValue):
    BEGIN = StateValue('begin')
    END = StateValue('end')
