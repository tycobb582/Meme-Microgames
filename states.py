import enum


class FnFStates(enum.Enum):
    P1_RECORD = 1
    P2_RECORD = 2
    P1_PLAY = 3
    P2_PLAY = 4
    IDLE = 5
    P1_WIN = 6
    P2_WIN = 7
