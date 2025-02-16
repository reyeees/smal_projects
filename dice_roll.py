#!/usr/bin/python3

# from https://github.com/reyeees/smal_projects
# Hi! This script contains dice rolling

# skin = {
#     "fill": "#",
#     "point": "*",
#     "fill_color": "\x1b[1;37m",
#     "pointer_color": "\x1b[1;31m"
# }

skin = {
    "fill": "█",
    "point": "■", # "•",
    "fill_color": "\x1b[1;37;107m",
    "pointer_color": "\x1b[1;31;107m"
}

import random
import time
import os

class App:
    def __init__(self) -> None:
        self.dice_sides = [
            f"{skin['fill_color']}{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}\n{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<11}\x1b[0m", 
            f"{skin['fill_color']}{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<8}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<8}\n{skin['fill']:{skin['fill']}<11}\x1b[0m", 
            f"{skin['fill_color']}{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<8}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<8}\n{skin['fill']:{skin['fill']}<11}\x1b[0m", 
            f"{skin['fill_color']}{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<11}\x1b[0m", 
            f"{skin['fill_color']}{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<11}\x1b[0m", 
            f"{skin['fill_color']}{skin['fill']:{skin['fill']}<11}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill_color']}{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<2}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<5}{skin['pointer_color']}{skin['point']}{skin['fill_color']}{skin['fill']:{skin['fill']}<2}\n{skin['fill']:{skin['fill']}<11}\x1b[0m"
        ]
        self.dice_pointer = 0
        self.sleep_step = 0.03
        self.clear = lambda: os.system("cls" if os.name == "nt" else "clear")

    def main(self) -> None:
        # ignore this, its for testing skins.
        # print(self.dice_sides)
        # for dice in self.dice_sides:
        #     print(dice, end = "\n")
        #     print('\n'.join(ascii(row) for row in dice.split('\n')), end = "\n\n")

        while True:
            sleep_count = 0.0
            for _ in range(0, random.randint(7, 20), 1):
                self.clear()

                if self.dice_pointer >= len(self.dice_sides):
                    self.dice_pointer = 0
                    random.shuffle(self.dice_sides)

                dice_side = self.dice_sides[self.dice_pointer]
                print(dice_side, end = "\n")
                
                time.sleep(sleep_count)

                self.dice_pointer += 1
                sleep_count += self.sleep_step
            print(f"Its {dice_side.count(skin['point'])}!")
            input("\x1b[8;0f<CTRL + C> for exit. <ENTER> for roll: ")
            # break

if __name__ == "__main__":
    App().main()