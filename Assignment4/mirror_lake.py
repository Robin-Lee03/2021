"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:blank_img_p2.red =
    :return:
    """
    new_img = SimpleImage(filename)
    blank_img = SimpleImage.blank(new_img.width, new_img.height * 2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            pixel = new_img.get_pixel(x,y)
            blank_img_p1 = blank_img.get_pixel(x,y)
            blank_img_p2 = blank_img.get_pixel(x,blank_img.height-y-1)

            blank_img_p1.red = pixel.red
            blank_img_p1.green = pixel.green
            blank_img_p1.blue = pixel.blue

            blank_img_p2.red = pixel.red
            blank_img_p2.green = pixel.green
            blank_img_p2.blue = pixel.blue

    return blank_img

def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
