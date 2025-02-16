# from https://github.com/reyeees/smal_projects
# Hi! This script is a small implementation of file explorer

import os
import glob

try:
    from pynput import keyboard
except ModuleNotFoundError:
    os.system("pip3 install pynput")
    from pynput import keyboard

class App:
    def __init__(self) -> None:
        self.selected_dirs_info = {}

        self.clear = lambda: os.system("cls" if os.name == "nt" else "clear")
        self.current_dir = os.getcwd()
        self.previous_dir = self.current_dir
        self.delimiter = "\\" if os.name == 'nt' else '/'

        self.selected = 0
        self.selected_file = ["", ""]
        
        self.first_dir = ""

    def on_press(self, key) -> None:
        if type(key) == keyboard._win32.KeyCode:
            if key.char == 'q':
                exit()
        else:
            if key == keyboard.Key.up:
                self.selected_dirs_info[self.current_dir] -= 1
                self.format_explorer()

            elif key == keyboard.Key.down:
                self.selected_dirs_info[self.current_dir] += 1
                self.format_explorer()

            elif key == keyboard.Key.left:
                # self.selected = 0
                self.previous_dir = self.current_dir
                self.current_dir = self.delimiter.join(self.current_dir.split(self.delimiter)[0:-1])
                self.format_explorer()

            elif key == keyboard.Key.right:
                # self.selected = 0
                self.previous_dir = self.current_dir
                self.current_dir = self.delimiter.join([self.current_dir, self.first_dir])
                self.format_explorer()

            elif key == keyboard.Key.enter:
                # self.selected = 0
                self.into_selected()
                if self.current_dir == "IN_FILE":
                    self.open_file()
                    self.current_dir = self.previous_dir
                self.format_explorer()

            elif key == keyboard.Key.backspace:
                # self.selected = 0
                self.current_dir = self.previous_dir
                self.format_explorer()

    def open_file(self) -> None:
        # if self.selected_file[1] in [33206]:
        self.clear()
        os.system(f"start \"{self.selected_file[0]}\"" if os.name == 'nt' else 'echo i\ dont\ know\ lol.')

    def into_selected(self) -> None:
        self.previous_dir = self.current_dir
        if self.selected_file[1] == 16895:
            self.current_dir = self.selected_file[0]
        else:
            self.current_dir = "IN_FILE"

    def format_explorer(self) -> None:
        if self.current_dir in self.selected_dirs_info.keys():
            self.selected = self.selected_dirs_info[self.current_dir]
        else:
            self.selected_dirs_info[self.current_dir] = 0
            self.selected = 0

        self.clear()
        print(self.current_dir, "\n--------------")
        files = glob.glob(self.current_dir + self.delimiter + "*", include_hidden = True)
        files.sort(key = lambda f: os.stat(f).st_mode != 16895)

        if self.selected < 0:
            self.selected = 0
        elif self.selected > len(files) - 1:
            self.selected = len(files) - 1

        if files != []:
            if os.stat(files[0]).st_mode == 16895:
                self.first_dir = files[0].split(self.delimiter)[-1]

            for file_ in enumerate(files):
                st_mode = os.stat(file_[1]).st_mode

                style = "\x1b[1m" if st_mode == 16895 else ''
                if file_[0] == self.selected:
                    self.selected_file = [file_[1], st_mode]
                    style += "\x1b[43m"

                print(f"{style}{file_[1].split(self.delimiter)[-1]}\x1b[0m", flush = True)
            # print(self.selected + 1, self.first_dir, self.selected_file, len(files), self.selected < 0, self.selected > len(files) - 1)
        else:
            print("\x1b[45m<EMPTY>\x1b[0m")

    def main(self) -> None:
        self.format_explorer()
        with keyboard.Listener(on_press = self.on_press, on_release = lambda key: None) as listener:
            listener.join()

if __name__ == "__main__":
    App().main()