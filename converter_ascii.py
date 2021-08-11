from PIL import Image
import sys


class ImageProcessing:

    ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    def __init__(self):
        self.image = None
        self.image_ascii = None
        self.image_size = None

    def open_image(self, path):
        try:
            image = Image.open(path)
        except ValueError:
            print(f'Cannot open this file: {path}\nPlease, try again...')
            self.open_image(input())
        else:
            self.image = image
            self.image_size = image.size

    def resize_image(self, new_width):
        width, height = self.image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        self.image = self.image.resize((new_width, new_height))
        self.image_size = self.image.size
        return self.image.size

    def grayify(self):
        return self.image.convert('L')

    def pixels_to_ascii(self):
        return ''.join([self.ASCII_CHARS[pixel // 25] for pixel in self.grayify().getdata()])

    def print_terminal(self):
        image_string_ascii = self.pixels_to_ascii()
        width = self.image_size[0]
        pixel_count = len(image_string_ascii)
        self.image_ascii = '\n'.join(image_string_ascii[i:(i + width)] for i in range(0, pixel_count, width))
        print(self.image_ascii)

    def save(self):
        with open('ascii_image.txt', 'w') as f:
            f.write(self.image_ascii)


path = sys.argv[1]
width = int(sys.argv[2])
image_jpeg = ImageProcessing()
image_jpeg.open_image(path)
image_jpeg.resize_image(width)
image_jpeg.print_terminal()
image_jpeg.save()
