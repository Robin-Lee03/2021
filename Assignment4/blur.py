"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width,img.width)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x,y)
            img_p_right = 0
            img_p_dr = 0
            img_p_down = 0
            img_p_left = 0
            img_p_ul = 0
            img_p_dl = 0
            img_p_up = 0
            img_p_ur = 0

            if x < img.width-1:
                img_p_right = img.get_pixel(x + 1, y)   # 右邊

                if y < img.height-1:
                    img_p_dr = img.get_pixel(x+1,y+1)    # 右下

            if y < img.height-1:
                img_p_down = img.get_pixel(x, y+1)   # 下面

            if x > 0:
                img_p_left = img.get_pixel(x-1,y)       # 左邊

                if y > 0:
                    img_p_ul = img.get_pixel(x-1,y-1)    # 左上

                if y < img.height-1:
                    img_p_dl = img.get_pixel(x-1, y+1)   # 左下

            if y > 0:
                img_p_up = img.get_pixel(x, y-1)         # 上面

                if x < img.width-1:
                    img_p_ur = img.get_pixel(x+1, y-1)   # 右上

            if x == 0 and y == 0:               # 左上角落

                new_pixel.red = (img_p_right.red + img_p_down.red + img_p_dr.red + img_p.red)/4
                new_pixel.green = (img_p_right.green + img_p_down.green + img_p_dr.green + img_p.green)/4
                new_pixel.blue = (img_p_right.blue + img_p_down.blue + img_p_dr.blue + img_p.blue)/4

            elif x == 0 and y == img.height - 1:  # 左下角落
                new_pixel.red = (img_p_up.red + img_p_ur.red + img_p_right.red + img_p.red)/4
                new_pixel.green = (img_p_up.green + img_p_ur.green + img_p_right.green + img_p.green)/4
                new_pixel.blue = (img_p_up.green + img_p_ur.green + img_p_right.green + img_p.green)/4

            elif x == img.width - 1 and y == 0:  # 右上角落

                    new_pixel.red = (img_p_left.red + img_p_dl.red + img_p_down.red + img_p.red)/4
                    new_pixel.green = (img_p_left.green + img_p_dl.green + img_p_down.green + img_p.green)/4
                    new_pixel.blue = (img_p_left.blue + img_p_dl.blue + img_p_down.blue + img_p.blue)/4

            elif x == img.width - 1 and y == img.height - 1:  # 右下角落
                    new_pixel.red = (img_p_up.red + img_p_ul.red + img_p_left.red + img_p.red)/4
                    new_pixel.green = (img_p_up.green + img_p_ul.green + img_p_left.green + img_p.green)/4
                    new_pixel.blue = (img_p_up.blue + img_p_ul.blue + img_p_left.blue + img_p.blue)/4

            elif y == 0 and 0 < x < img.width - 1:  # 上方靠牆

                    new_pixel.red = (img_p_left.red + img_p_dl.red + img_p_down.red + img_p_dr.red + img_p_right.red
                                     + img_p.red)/6
                    new_pixel.green = (img_p_left.green + img_p_dl.green + img_p_down.green + img_p_dr.green
                                       + img_p_right.green + img_p.green)/6
                    new_pixel.blue = (img_p_left.blue + img_p_dl.blue + img_p_down.blue + img_p_dr.blue
                                       + img_p_right.blue + img_p.blue)/6

            elif y == img.height - 1 and 0 < x < img.width - 1: # 下方靠牆

                new_pixel.red = (img_p_left.red + img_p_right.red + img_p_ul.red + img_p_up.red
                                 + img_p_ur.red + img_p.red)/6
                new_pixel.green = (img_p_left.green + img_p_right.green + img_p_ul.green + img_p_up.green
                                 + img_p_ur.green + img_p.green)/6
                new_pixel.blue = (img_p_left.blue + img_p_right.blue + img_p_ul.blue + img_p_up.blue
                                 + img_p_ur.blue + img_p.blue)/6

            elif x == 0 and 0 < y < img.height - 1: # 左方靠牆

                new_pixel.red = (img_p_up.red + img_p_down.red + img_p_ur.red + img_p_right.red + img_p_dr.red
                                 + img_p.red)/6
                new_pixel.green = (img_p_up.green + img_p_down.green + img_p_ur.green + img_p_right.green
                                   + img_p_dr.green + img_p.green)/6
                new_pixel.blue = (img_p_up.blue + img_p_down.blue + img_p_ur.blue + img_p_right.blue
                                   + img_p_dr.blue + img_p.blue)/6

            elif x == img.width - 1 and 0 < y < img.height - 1:  # 右方靠牆

                new_pixel.red = (img_p_up.red + img_p_down.red + img_p_ul.red + img_p_left.red + img_p_dl.red
                                 + img_p.red)/6
                new_pixel.green = (img_p_up.green + img_p_down.green + img_p_ul.green + img_p_left.green
                                   + img_p_dl.green + img_p.green)/6
                new_pixel.blue = (img_p_up.blue + img_p_down.blue + img_p_ul.blue + img_p_left.blue
                                   + img_p_dl.blue + img_p.blue)/6

            else:

                new_pixel.red = (img_p_ul.red + img_p_left.red + img_p_dl.red + img_p_down.red + img_p_dr.red +
                                 img_p_right.red + img_p_ur.red + img_p_up.red + img_p.red) // 9
                new_pixel.green = (img_p_ul.green + img_p_left.green + img_p_dl.green + img_p_down.green +
                                   img_p_dr.green + img_p_right.green + img_p_ur.green + img_p_up.green
                                   + img_p.green) // 9
                new_pixel.blue = (img_p_ul.blue + img_p_left.blue + img_p_dl.blue + img_p_down.blue + img_p_dr.blue +
                                  img_p_right.blue + img_p_ur.blue + img_p_up.blue + img_p.blue) // 9

    return new_img

def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
