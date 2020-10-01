from typing import Iterable

from .types import Symbol, State, Direction


class TuringStep():
    def __init__(self, state: State, symbol: Symbol):
        self.state = state
        self.symbol = symbol

    def __str__(self) -> str:
        return f'[{self.state}:\'{self.symbol}\']'

    def __eq__(self, o: object) -> bool:
        assert isinstance(
            o, TuringStep), 'TuringStep can only be test with TuringStep'
        return self.state == o.state and self.symbol == o.symbol


class TuringAction():
    def __init__(self, from_step: TuringStep, to_step: TuringStep, target_direction: Direction):
        self.from_step = from_step
        self.to_step = to_step
        self.target_direction = target_direction

    def match(self, step: TuringStep) -> bool:
        return self.from_step == step

    def exec(self):
        return self.to_step, self.target_direction


class TuringMemory():
    def __init__(self, tape: Iterable[Symbol], head=0) -> None:
        self.state = State.BEGIN
        self.tape = tape
        self.head = head
        self.step = TuringStep(self.state, self.tape[self.head])
        self.step_index = 0

    def __str__(self) -> str:
        begin, end = self.tape[:self.head], self.tape[self.head+1:]
        return ''.join([*begin, '[', self.tape[self.head], ']', *end])

    def _resize_if_needed(self):
        last = len(self.tape) - 1
        if self.head < 0:
            self.tape = ([Symbol.NEUTRAL] * (-self.head)) + self.tape
            self.head = 0
        elif self.head > last:
            self.tape = self.tape + ([Symbol.NEUTRAL] * (self.head-last))
            self.head = last

    def get_state(self):
        return self.state

    def get_step(self):
        return self.step

    def write_symbol(self, symbol: Symbol):
        self._resize_if_needed()
        self.tape[self.head] = symbol

    def get_symbol(self):
        self._resize_if_needed()
        return self.tape[self.head]

    def make_step(self, step: TuringStep, direction: Direction):
        print(
            f'STEP {self.step_index}:\n  memory\t{self}\n  state\t\t{self.step.state} -> {step.state}\n  write\t\t"{step.symbol}"\n  move\t\t{direction}', end='\n\n')
        self.write_symbol(step.symbol)
        if direction == Direction.LEFT:
            self.head += -1
        elif direction == Direction.RIGHT:
            self.head += 1
        self.state = step.state
        self.step = TuringStep(step.state, self.get_symbol())
        self.step_index += 1
