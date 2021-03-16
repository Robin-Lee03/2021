"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:
    """

    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_img_p = figure_img.get_pixel(x, y)
            background_img_p = background_img.get_pixel(x,y)
            bigger = max(figure_img_p.red,figure_img_p.blue)
            if figure_img_p.green > bigger * 2:
                figure_img_p.red = background_img_p.red
                figure_img_p.green = background_img_p.green
                figure_img_p.blue = background_img_p.blue

    return figure_img


def main():
    """
    TODO:
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
