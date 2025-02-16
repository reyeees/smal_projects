# from https://github.com/reyeees/smal_projects
# Hi! This script is a terminal implementation of monkeytype.com

import os
import time

try:
    from pynput import keyboard
except ModuleNotFoundError:
    os.system("pip3 install pynput")
    from pynput import keyboard

from pynput.keyboard import Key as keys

class App:
    def __init__(self) -> None:
        self.info = {
            "missteps": 0,
            "backspaces": 0,
            "time": 0
        }
        self.words = "hello world"
        self.typed = ""
        self.clear = lambda: os.system('cls||clear')

        self.start_time = 0
        self.mode = True

    def check(self) -> None:
        for char in enumerate(self.typed):
            if char[1] != self.words[char[0]]:
                self.info['missteps'] += 1
        
        self.clear()
        print(f"Original: {self.words}\nResult: {self.typed}\nChars: {len(self.words)}\nWords: {len(self.words.split(' '))}\nMissteps: {self.info['missteps']}\nBackSpaces: {self.info['backspaces']}\nTime: {self.info['time']}\n\nPress any button for exit.")

    def typing(self, key) -> None:
        if self.mode:
            self.clear()

            if self.typed == "" and self.info['backspaces'] == 0:
                self.start_time = time.time()

            if type(key) == keyboard._win32.KeyCode:
                self.typed += key.char
            else:
                if key == keys.backspace:
                    self.typed = self.typed[0:-1]
                    self.info["backspaces"] += 1
                
                if key == keys.space:
                    self.typed += " "

                if key == keys.esc:
                    exit()
            print(f"\x1b[90m{self.words}\x1b[1;0f\x1b[0m{self.typed}", end = "", flush = True)

            if len(self.typed) == len(self.words):
                self.info['time'] = time.time() - self.start_time
                self.mode = False
                self.check()
        else:
            exit()
            # raise Exception("Leaving from program..")

    def main(self) -> None:
        self.clear()
        print(f"Ready.\n\x1b[90m{self.words}", end = "\r", flush = True)
        with keyboard.Listener(on_press = self.typing, on_release = lambda key: None) as listener:
            listener.join()

if __name__ == "__main__":
    App().main()