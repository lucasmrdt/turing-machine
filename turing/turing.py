from sys import stderr
from typing import Iterable

from turing.programs import PROGRAMS
from .utils import TuringAction, TuringMemory
from .types import Symbol, State
from .errors import NoTuringActionFoundException


class TuringProgram():
    def __init__(self, pgrm: Iterable[TuringAction], input: Iterable[Symbol], head=0):
        self.pgrm = pgrm
        self.memory = TuringMemory(list(input), head=head)

    def _get_action(self):
        action_to_exec = None
        memory = self.memory
        for action in self.pgrm:
            if action.match(memory.get_step()):
                action_to_exec = action
                break
        if not action_to_exec:
            raise NoTuringActionFoundException(str(memory.get_step()))
        return action_to_exec

    def run(self):
        while self.memory.get_state() != State.END:
            action_to_exec = self._get_action()
            new_step, direction = action_to_exec.exec()
            self.memory.make_step(new_step, direction)
        print(self.memory)


def load_package():
    pgrm_keys = list(PROGRAMS.keys())
    pgrm_list = '\n'.join(f'{i}) {name}' for i,
                          name in enumerate(pgrm_keys))
    print(f'Select your program :\n\n{pgrm_list}\n')
    while True:
        try:
            selected_index = int(input('> '))
            assert 0 <= selected_index < len(pgrm_keys)
        except (ValueError, AssertionError):
            print('Bad input', file=stderr)
            continue
        break
    return PROGRAMS[pgrm_keys[selected_index]]


def main():
    package = load_package()
    pgrm = TuringProgram(package.PROGRAM, package.INPUT)
    pgrm.run()
