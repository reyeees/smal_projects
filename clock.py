# from https://github.com/reyeees/smal_projects
# Hi! This script shows fancy clock in terminal window

import os
import sys
from time import strftime
from functools import cache

try:
    from pyfiglet import Figlet
except ModuleNotFoundError:
    os.system("pip3 install pyfiglet")
    from pyfiglet import Figlet

class App:
    def __init__(self) -> None:
        self.font = Figlet(font = "doom")
        self.terminal_size = self.get_size()
        self.alarm = " 11:02:11"

    def get_size(self) -> os.terminal_size:
        try:
            columns: int = int(os.environ["COLUMNS"])
        except (KeyError, ValueError): 
            columns: int = 0
        try:
            lines: int = int(os.environ["LINES"])
        except (KeyError, ValueError): 
            lines: int = 0

        if columns <= 0 or lines <= 0:
            try: 
                size: os.terminal_size = os.get_terminal_size(sys.__stdout__.fileno())
            except (AttributeError, ValueError, OSError): 
                size: os.terminal_size = os.terminal_size((80, 24))

            if columns <= 0: 
                columns = size.columns or 80
            if lines <= 0: 
                lines = size.lines or 24
        return os.terminal_size((columns, lines))

    def format(self, text) -> None:
        columns = (len(text[0]) + (self.terminal_size[0] - len(text[0]))) // 2 - 10

        return '\n'.join([
            f"+{'-':-^{columns - 2}}+", 
            '\n'.join([f"|{row:<{columns - 2}}|" for row in filter(lambda row: row.strip() != '', text)]), 
            f"+{'-':-^{columns - 2}}+"
        ])

    def main(self) -> None:
        os.system("cls||clear")
        while True:
            print("\x1b[0;0f", end = "", flush = True)
            time = strftime(" %H:%M:%S")
            print(self.format(self.font.renderText(time).split("\n")), end = "", flush = True)
            # if time == self.alarm:
                # break

if __name__ == "__main__":
    App().main()