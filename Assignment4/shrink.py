"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    new_img = SimpleImage(filename)
    blank_img = SimpleImage.blank(new_img.width // 2, new_img.height // 2)
    # new_img.make_as_big_as(blank_img)

    for x in range(new_img.width):
        for y in range(new_img.height):
            pixel = new_img.get_pixel(x, y)
            blank_img_p = blank_img.get_pixel(x//2, y//2)

            if x % 2 == 0 and y % 2 == 0:
                blank_img_p.red = pixel.red
                blank_img_p.green = pixel.green
                blank_img_p.blue = pixel.blue

    return blank_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
