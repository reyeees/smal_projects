# from https://github.com/reyeees/smal_projects
# Hi! This script is supposed to put pixels of image on chess desk grid in form of chess cases

from PIL import Image, ImageDraw, ImageFont, ImageEnhance

class App:
    def __init__(self) -> None:
        self.natural_color: bool = False
        
        self.char_size = (12, 12)
        self.font = ImageFont.truetype('casefont.ttf', 12)
        self.cases = "bknpqr lmotvw".split(" ")

        self.image = ImageEnhance.Contrast(
                        ImageEnhance.Brightness(Image.open("1.png")).enhance(1.5)
                    ).enhance(1.5).convert("L") # wtf
                    #  Image.open("1.png")\
                    #     .point(lambda c: 128 + (259 * (50 + 255)) / (255 * (259 - 50)) * (c - 128))\
                    #         .convert("L")
        # self.image.show()
        self.image = self.image.resize(
            (int(0.09 * self.image.size[0]), 
             int(0.09 * self.image.size[1] * (self.char_size[0] / self.char_size[1]))), 
            Image.Resampling.NEAREST
        )
        self.pixels = self.image.load()

    def main(self) -> None:
        self.result_image = Image.new("RGB", self.image.size, (241, 215, 180))
        for y in range(0, self.image.size[1], 1):
            for x in range(0, self.image.size[0], 1):
                if (x + y) % 2:
                    self.result_image.putpixel((x, y), (185, 136, 96))

        self.result_image = self.result_image.resize(
            (self.char_size[0] * self.image.size[0],
             self.char_size[1] * self.image.size[1]), 
            Image.Resampling.NEAREST
        )
        self.draw = ImageDraw.Draw(self.result_image)

        for y in range(0, self.image.size[1], 1):
            for x in range(0, self.image.size[0], 1):
                color = self.pixels[x, y] + 50

                if self.natural_color == False:
                    char_color = (color, color, color)
                    cases = self.cases[1]
                elif color > 50:
                    char_color = (255, 255, 255)
                    cases = self.cases[1]
                else:
                    char_color = (0, 0, 0)
                    cases = self.cases[0]

                self.draw.text(
                    (x * self.char_size[0], y * self.char_size[1]), 
                    cases[int(self.pixels[x, y] * 0.0234375)],
                    char_color, self.font
                )

        self.result_image.save("2.png")

App().main()