from typing import Dict, Final


class COLORS:
    BLUE: Final[str] = '\033[94m'
    YELLOW: Final[str] = '\033[93m'
    RED: Final[str] = '\033[91m'
    GREEN: Final[str] = '\033[92m'
    MAGENTA: Final[str] = '\033[96m'
    CYAN: Final[str] = '\033[96m'
    RESET: Final[str] = '\033[0m'


def get_color(note: str, chord_hist: Dict[str, int]) -> str:
    if chord_hist[note] >= 5:
        return COLORS.RED
    if chord_hist[note] >= 4:
        return COLORS.BLUE
    if chord_hist[note] >= 3:
        return COLORS.GREEN
    if chord_hist[note] >= 2:
        return COLORS.YELLOW
    else:
        return COLORS.RESET


def color(message: str, color) -> str:
    return f'{color}{message}{COLORS.RESET}'

