class NoTuringActionFoundException(Exception):
    def __init__(self, explanation: str):
        super().__init__(f'No Turing Action Found in step: {explanation}')
