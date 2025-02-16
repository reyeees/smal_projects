# From https://github.com/reyeees/smal_projects
# Hi! This script is supposed to take text, put characters into RGB values and turn it into image.
# It can also decode this


from PIL import Image
from random import randint
from functools import cache

class Decode:
    def __init__(self) -> None:
        self.image = Image.open("1.png")
        self.pixels = self.image.load()
        self.result = open("encoded_1.png.txt", 'wb')

    @cache
    def main(self) -> None:
        for y in range(0, self.image.size[1], 1):
            for x in range(0, self.image.size[0], 1):
                self.result.write(eval('b' + ascii(chr(self.pixels[x, y][0]))))
                # self.result = ''.join([self.result, chr(sum(self.pixels[x, y]))])

        self.result.close()

class App:
    def __init__(self) -> None:
        self.max_size = [512, 512]
        self.use_max_size = True
        self.message = "доброго ранку."
        self.word = self.format(self.message)
        self.image = Image.new("RGBA", self.max_size, color = (0, 0, 0, 0))
        self.pixels = self.image.load()

    @cache
    def format(self, text: str) -> list[bytes]:
        result = []
        if self.use_max_size:
            size = [self.max_size[0], 0]
            for i in range(0, len(text), self.max_size[0]):
                result.append(f"{text[i: i + self.max_size[0]]:<{self.max_size[0]}}".encode())
                size[1] += 1

                if size[1] >= self.max_size[1]:
                    self.max_size = size
            if size[1] < self.max_size[1]:
                for i in range(0, self.max_size[1] - size[1], 1):
                    result.append(f"{' ':<{self.max_size[0]}}".encode())
        else:
            size = [len(text.encode()), 1]
            result.append(text.encode())
            self.max_size = size
        return result

    @cache
    def main(self) -> None:
        for y in range(0, self.max_size[1], 1):
            for x in range(0, self.max_size[0], 1):
                if self.word[y][x] >= 255:
                    print(self.word[y][x])
                self.pixels[x, y] = (self.word[y][x], randint(0, 255), randint(0, 255), randint(0, 255))
        self.image.save("1.png")

if __name__ == "__main__":
    App().main()
    Decode().main()