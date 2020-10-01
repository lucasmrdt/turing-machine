from enum import Enum

from turing.utils import TuringAction, TuringStep
from turing.types import Direction, State, Symbol, StateValue, SymbolValue


class ExtendedState(State):
    GO_TO_RIGHT = StateValue('go-to-right')
    GO_TO_LEFT = StateValue('go-to-left')
    BACK_TO_START = StateValue('back-to-start')
    INCREASE_NUMBER_SPACE = StateValue('increase-number-space')


class ExtendedSymbol(Symbol):
    ZERO = SymbolValue('0')
    ONE = SymbolValue('1')
    ADD = SymbolValue('+')
    LEFT = SymbolValue('^')
    RIGHT = SymbolValue('$')


PROGRAM = [
    # Step 1 : Go to the most right
    TuringAction(
        from_step=TuringStep(state=ExtendedState.BEGIN,
                             symbol=ExtendedSymbol.LEFT),
        to_step=TuringStep(state=ExtendedState.GO_TO_RIGHT,
                           symbol=ExtendedSymbol.LEFT),
        target_direction=Direction.RIGHT
    ),
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.GO_TO_RIGHT, symbol=ExtendedSymbol.ZERO),
        to_step=TuringStep(state=ExtendedState.GO_TO_RIGHT,
                           symbol=ExtendedSymbol.ZERO),
        target_direction=Direction.RIGHT
    ),
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.GO_TO_RIGHT, symbol=ExtendedSymbol.ONE),
        to_step=TuringStep(state=ExtendedState.GO_TO_RIGHT,
                           symbol=ExtendedSymbol.ONE),
        target_direction=Direction.RIGHT
    ),

    # Step 2 : Replace all right ones with zeros
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.GO_TO_RIGHT, symbol=ExtendedSymbol.RIGHT),
        to_step=TuringStep(state=ExtendedState.GO_TO_LEFT,
                           symbol=ExtendedSymbol.RIGHT),
        target_direction=Direction.LEFT
    ),
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.GO_TO_LEFT, symbol=ExtendedSymbol.ONE),
        to_step=TuringStep(state=ExtendedState.GO_TO_LEFT,
                           symbol=ExtendedSymbol.ZERO),
        target_direction=Direction.LEFT
    ),

    # Step 3 : Replace the first zero with one and terminate the turing machine
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.GO_TO_LEFT, symbol=ExtendedSymbol.ZERO),
        to_step=TuringStep(state=ExtendedState.BACK_TO_START,
                           symbol=ExtendedSymbol.ONE),
        target_direction=Direction.LEFT
    ),

    # Step 3.a : If the number is only composed of ones we increased the number space on the right
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.GO_TO_LEFT, symbol=ExtendedSymbol.LEFT),
        to_step=TuringStep(
            state=ExtendedState.INCREASE_NUMBER_SPACE, symbol=ExtendedSymbol.ONE),
        target_direction=Direction.LEFT
    ),
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.INCREASE_NUMBER_SPACE, symbol=ExtendedSymbol.NEUTRAL),
        to_step=TuringStep(state=ExtendedState.END,
                           symbol=ExtendedSymbol.LEFT),
        target_direction=Direction.NOT_MOVE
    ),


    # Step 3.b : Move the head to the starting point
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.BACK_TO_START, symbol=ExtendedSymbol.ONE),
        to_step=TuringStep(state=ExtendedState.BACK_TO_START,
                           symbol=ExtendedSymbol.ONE),
        target_direction=Direction.LEFT
    ),
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.BACK_TO_START, symbol=ExtendedSymbol.ZERO),
        to_step=TuringStep(state=ExtendedState.BACK_TO_START,
                           symbol=ExtendedSymbol.ZERO),
        target_direction=Direction.LEFT
    ),
    TuringAction(
        from_step=TuringStep(
            state=ExtendedState.BACK_TO_START, symbol=ExtendedSymbol.LEFT),
        to_step=TuringStep(state=ExtendedState.END,
                           symbol=ExtendedSymbol.LEFT),
        target_direction=Direction.NOT_MOVE
    ),
]

INPUT = [
    ExtendedSymbol.LEFT,
    ExtendedSymbol.ONE,
    ExtendedSymbol.ONE,
    ExtendedSymbol.ONE,
    ExtendedSymbol.RIGHT,
]
