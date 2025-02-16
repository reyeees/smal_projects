# from https://github.com/reyeees/smal_projects
# Hi! This script is supposed to put text on images, saving color of pixels

from PIL import Image, ImageDraw, ImageFont
from argparse import ArgumentParser

class App:
    def __init__(self, image: str) -> None:
        self.format = lambda text: [
            f"{text[i: i + self.image.size[0]]:<{self.image.size[0]}}" \
                for i in range(0, len(text), self.image.size[0])
        ]
        self.filename = image
        self.image = Image.open(image)# .convert("L").convert("RGB")
        self.char_size = (30, 38)
        self.resized = self.image.resize(
            (int(0.09 * self.image.size[0]), 
             int(0.09 * self.image.size[1] * (self.char_size[0] / self.char_size[1]))), 
            Image.Resampling.NEAREST
        )
        self.words = self.format(
            open("1.txt", "r", encoding = "utf-8").read()\
                .replace("\t", "    ").replace("\n", " ")
        )
        self.font = ImageFont.truetype('C:\\Windows\\Fonts\\consola.ttf', 45)
        self.pixels = self.resized.load()
        self.result_image = Image.new(
            "RGBA", 
            (self.char_size[0] * self.resized.size[0],
             self.char_size[1] * self.resized.size[1]), 
            (0, 0, 0, 0) # (0, 0, 0)
        )
        self.draw = ImageDraw.Draw(self.result_image)

    def main(self) -> None:
        for y in range(0, self.resized.size[1], 1):
            for x in range(0, self.resized.size[0], 1):
                # self.draw.text(
                #     (x * self.char_size[0], y * self.char_size[1]),
                #     self.words[y][x],
                #     (0, 0, 0, 255),# (255, 255, 255),
                #     self.font
                # )
                self.draw.text(
                    (x * self.char_size[0], y * self.char_size[1]), 
                    self.words[y][x], 
                    self.pixels[x, y], 
                    self.font
                )
        # self.result_image = self.result_image.resize(self.image.size, Image.Resampling.NEAREST)
        # self.image = Image.composite(
        #     Image.new("RGB", self.image.size, (0, 0, 0)),
        #     self.image,
        #     self.result_image
        # )
        # # self.image.paste(
        #     # self.result_image,
        #     # (0, 0), 
        #     # self.result_image# .convert("L")
        # # )
        self.result_image.convert("RGB").show()
        self.result_image.convert("RGB").resize((self.result_image.size[0] * 2, self.result_image.size[1] * 2))\
            .save(self.filename.split(".")[0] + "_out.jpg")
        # self.image.show()
        # self.image.save(self.filename.split(".")[0] + "_maskedout.png")

if __name__ == "__main__":
    parser = ArgumentParser(description = "Images with words generator by ReYeS")
    parser.add_argument("path", help = "Path to image.", type = str)
    args = parser.parse_args()
    del parser
    App(args.path).main()