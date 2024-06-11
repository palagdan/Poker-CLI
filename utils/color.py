from enum import Enum


class Color(Enum):
    """
    An enumeration representing ANSI color codes for text and background colors.

    Attributes:
        BLACK: ANSI escape code for black text.
        RED: ANSI escape code for red text.
        GREEN: ANSI escape code for green text.
        YELLOW: ANSI escape code for yellow text.
        BLUE: ANSI escape code for blue text.
        MAGENTA: ANSI escape code for magenta text.
        CYAN: ANSI escape code for cyan text.
        LIGHT_GRAY: ANSI escape code for light gray text.
        DARK_GRAY: ANSI escape code for dark gray text.
        BRIGHT_RED: ANSI escape code for bright red text.
        BRIGHT_GREEN: ANSI escape code for bright green text.
        BRIGHT_YELLOW: ANSI escape code for bright yellow text.
        BRIGHT_BLUE: ANSI escape code for bright blue text.
        BRIGHT_MAGENTA: ANSI escape code for bright magenta text.
        BRIGHT_CYAN: ANSI escape code for bright cyan text.
        WHITE: ANSI escape code for white text.
        RESET: ANSI escape code to reset text color.
        BACKGROUND_BLACK: ANSI escape code for black background.
        BACKGROUND_RED: ANSI escape code for red background.
        BACKGROUND_GREEN: ANSI escape code for green background.
        BACKGROUND_YELLOW: ANSI escape code for yellow background.
        BACKGROUND_BLUE: ANSI escape code for blue background.
        BACKGROUND_MAGENTA: ANSI escape code for magenta background.
        BACKGROUND_CYAN: ANSI escape code for cyan background.
        BACKGROUND_LIGHT_GRAY: ANSI escape code for light gray background.
        BACKGROUND_DARK_GRAY: ANSI escape code for dark gray background.
        BACKGROUND_BRIGHT_RED: ANSI escape code for bright red background.
        BACKGROUND_BRIGHT_GREEN: ANSI escape code for bright green background.
        BACKGROUND_BRIGHT_YELLOW: ANSI escape code for bright yellow background.
        BACKGROUND_BRIGHT_BLUE: ANSI escape code for bright blue background.
        BACKGROUND_BRIGHT_MAGENTA: ANSI escape code for bright magenta background.
        BACKGROUND_BRIGHT_CYAN: ANSI escape code for bright cyan background.
        BACKGROUND_WHITE: ANSI escape code for white background.
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BACKGROUND_BLACK = '\033[40m'
    BACKGROUND_RED = '\033[41m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_YELLOW = '\033[43m'
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_MAGENTA = '\033[45m'
    BACKGROUND_CYAN = '\033[46m'
    BACKGROUND_LIGHT_GRAY = '\033[47m'
    BACKGROUND_DARK_GRAY = '\033[100m'
    BACKGROUND_BRIGHT_RED = '\033[101m'
    BACKGROUND_BRIGHT_GREEN = '\033[102m'
    BACKGROUND_BRIGHT_YELLOW = '\033[103m'
    BACKGROUND_BRIGHT_BLUE = '\033[104m'
    BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
    BACKGROUND_BRIGHT_CYAN = '\033[106m'
    BACKGROUND_WHITE = '\033[107m'


def print_with_color(text, color, end='\n'):
    """
    Prints text with the specified color.

    Args:
        text (str): The text to print.
        color (Color): The color to apply to the text.
        end (str, optional): The string appended after the last value, defaults to newline ('\n').
    """
    print(color.value + text + Color.RESET.value, end=end)
