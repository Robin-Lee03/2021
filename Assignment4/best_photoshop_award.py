"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1.3

def main():
    """
    TODO:
    """
    robin_img = SimpleImage('images/robin.jpg')
    shakehand_img = SimpleImage('images/shakehand.jpg')
    shakehand_img.make_as_big_as(robin_img)
    for x in range(robin_img.width):
        for y in range(robin_img.height):
            robin_pixel = robin_img.get_pixel(x,y)
            avg = (robin_pixel.red + robin_pixel.green + robin_pixel.blue)//3
            if robin_pixel.green > avg * THRESHOLD:
                shakehand_pixel = shakehand_img.get_pixel(x,y)
                robin_pixel.red = shakehand_pixel.red
                robin_pixel.green = shakehand_pixel.green
                robin_pixel.blue = shakehand_pixel.blue

    robin_img.show()

if __name__ == '__main__':
    main()
