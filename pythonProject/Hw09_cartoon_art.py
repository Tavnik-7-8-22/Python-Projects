"""
Project:      hw09-Pop_Art.py
Description: Turns a regular image into pop art
Name: Samuel Rabinor
Date: 12/9/22
Notes:          Install the Pillow library.

                >Open PyCharm > Preferences:
                >Find your project and click "Project Interpreter"
                >Click the "+" (in the bottom left)
                >Search for Pillow and select it
                >Check the box to "install to user's package library"
                >Click "Install Package"

                Or, the Terminal enter the following:
                sudo pip install Pillow

You may need to update pip in order to uninstall Pillow. In terminal do the following:  sudo pip install --upgrade pip
"""
# -------------------------------------------------------------------------------


from PIL.Image import open, new
from PIL.ImageColor import getrgb
from PIL.ImageOps import grayscale


class PopArt:
    """
    The PopArt class will open an image file and modify the image
    to turn it into "Pop Art."
    """

    def __init__(self, img):
        """
        This is the constructor, where instance variables are initialized.
        """
        self.palette = ['66A3D2', '0B61A4', '67E300', 'A62F20', '3F92D2']
        self.img = open(img)

    def hex_to_rgb(self, hex):
        """
        Convert a given color value from a hexadecimal value to a rgb tuple. For example a hex value of "C9A814"
        would get converted to (201, 168, 20).
        :param hex: A String with the hexadecimal value to convert
        :return: A tuple containing the rgb values
        """
        return getrgb('#' + hex)  # convert to hex value

    def rgb_to_hex(self, rgb):
        """
        Convert a given color value from a rgb tuple to a hexadecimal value. For example a rgb
        value of (201, 168, 20) would get converted to C9A814.
        :param rgb: A tuple with the rgb value to convert
        :return: A string containing the hexadecimal value
        """
        # 02 means 2 "digits" and X means hex (IN UPPER CASE), so each r g b value is turned into 2 hex "digits"
        hex_value = '{0:02X}{1:02X}{2:02X}'.format(rgb[0], rgb[1], rgb[2])
        return hex_value

    def process_image(self):
        """
        The process that turns the image to gray scale, to cartoon, to pop art.
        :return: A pop art version of the input image
        """
        gray_image = grayscale(self.img)  # convert image to grayscale
        print("displaying grayscale image...")
        gray_image.show()
        gray_pixels = gray_image.getdata()  # get a PIL sequence of pixel value
        pix_list = []  # create empty list
        for gp in gray_pixels:
            if 50 < gp < 100:  # notice simplified if condition
                pix_list.append(gp)  # add pixels to list
        for i in range(10):
            print(gray_pixels[i], end=" ")
        print()
        new_img_pixels = self.make_cartoon_pic(gray_pixels)  # uses grayscale to turn original image into "cartoon" image
        w, h = self.img.size
        print("initializing image comparison...")
        print("img total pixels:", w * h)
        print("new_img total pixels:", len(new_img_pixels))
        assert (w * h == len(new_img_pixels))  # makes sure that the pixels in old and new image are equal
        img = new("RGB", self.img.size)
        img.putdata(new_img_pixels)
        print("displaying cartoon image...")
        img.show()  # shows "cartoon" image
        img = self.make_dots(img, self.palette[4])
        img.save("art_dot.bmp")
        print("displaying dotted cartoon image...")
        img.show()  # shows cartoon image with added dots
        img = self.make_lines(img, self.palette[2])
        img.save("cartoon_art.bmp")
        print("displaying dotted + lined cartoon image...")
        img.show()  # shows cartoon image with added lines
        img = self.make_pattern(img, self.palette[1])
        img.save("cross_hatchet.bmp")
        print("displaying dotted + lined + plus symboled image...")
        img.show()  # shows cartoon image with added plus symbols

    def make_cartoon_pic(self, pixels):
        """
        Changes the pixels in the grayscale image to pixels on the palette.
        :param pixels: The pixels found in the grayscale image
        :return: The converted pixels
        """
        new_pixels = []
        for p in pixels:
            if p <= 51:
                new_pixels.append(self.hex_to_rgb(self.palette[0]))  # Changes any pixel within the color range of 0 - 51 to palette 0
            elif p <= 102:
                new_pixels.append(self.hex_to_rgb(self.palette[1]))  # Changes any pixel within the color range of 52 - 102 to palette 1
            elif p <= 153:
                new_pixels.append(self.hex_to_rgb(self.palette[2]))  # Changes any pixel within the color range of 103 - 153 to palette 2
            elif p <= 204:
                new_pixels.append(self.hex_to_rgb(self.palette[3]))  # Changes any pixel within the color range of 154 - 204 to palette 3
            elif p <= 255:
                new_pixels.append(self.hex_to_rgb(self.palette[4]))  # Changes any pixel within the color range of 205 - 255 to palette 4
        return new_pixels

    def make_dots(self, base_image, hex_color):
        """
        Adds dots to the cartoon image
        :param base_image: The image were adding the dots to.
        :param hex_color: The color to which we should add the dots.
        :return: The cartoon image with added dots.
        """
        w, h = self.img.size  # get the image width and height
        for x in range(0, w, 10):  # loop through x values
            for y in range(0, h, 10):  # for each x value, loop through y values
                p = base_image.getpixel((x, y))  # get the pixel color
                if p == self.hex_to_rgb(hex_color):
                    base_image.putpixel((x, y), (0, 0, 0))  # if the pixel matches the color of the hex color add a dot
        return base_image

    def make_lines(self, base_image, hex_color):
        """
               Adds lines to the cartoon image
               :param base_image: The image were adding the lines to.
               :param hex_color: The color to which we should add the lines.
               :return: The cartoon image with added lines.
               """
        w, h = self.img.size  # get the image width and height
        for x in range(0, w, 10):  # loop through x values
            for y in range(h):  # for each x value, loop through y
                p = base_image.getpixel((x, y))  # get the pixel color
                if p == self.hex_to_rgb(hex_color):
                    base_image.putpixel((x, y), (0, 255, 0, 224))  # if the pixel matches the color of the hex color add a line
        return base_image

    def make_pattern(self, base_image, hex_color):
        """
               Adds plus symbols to the cartoon image
               :param base_image: The image were adding the plus symbols to.
               :param hex_color: The color to which we should add the plus symbols.
               :return: The cartoon image with added plus symbols.
               """
        count = 0  # initialize count variable
        w, h = self.img.size  # get the image width and height
        for x in range(0, w - 1, 10):  # loop through x values
            for y in range(0, h, 10):   # for each x value, loop through y values
                p = base_image.getpixel((x, y))  # get the pixel color
                if p == self.hex_to_rgb(hex_color):
                    base_image.putpixel((x, y), (102, 102, 255))  # if the pixel matches the color of the hex color add a dot
                    count += 1  # mark middle dot as placed
                    if count == 1:
                        base_image.putpixel((x - 1, y), (102, 102, 255))  # add a pixel before the dot
                        base_image.putpixel((x, y - 1), (102, 102, 255))  # add a pixel below the dot
                        base_image.putpixel((x, y + 1), (102, 102, 255))  # add a pixel above the dot
                        base_image.putpixel((x + 1, y), (102, 102, 255))  # add a pixel after the dot
                        count -= 1  # mark plus symbol as added
        for x in range(5, w, 10):  # loop through x values with a slight offset
            for y in range(5, h - 1, 10):  # for each x value, loop through y values with a slight offset
                p = base_image.getpixel((x, y))  # get the pixel color
                if p == self.hex_to_rgb(hex_color):
                    base_image.putpixel((x, y), (102, 102, 255))  # if the pixel matches the color of the hex color add a dot
                    count += 1  # initiate count variable
                    if count == 1: # mark middle dot as placed
                        base_image.putpixel((x - 1, y), (102, 102, 255))  # add a pixel before the dot
                        base_image.putpixel((x, y - 1), (102, 102, 255))  # add a pixel below the dot
                        base_image.putpixel((x, y + 1), (102, 102, 255))  # add a pixel above the dot
                        base_image.putpixel((x + 1, y), (102, 102, 255))  # add a pixel after the dot
                        count -= 1 # mark plus symbol as added
        return base_image


if __name__ == '__main__':  # run the program only if this is the code file we're working on
    pop = PopArt('wave.bmp')  # use this line after you add the parameter to the constructor
    pop.process_image()  # call the process function to run the program
