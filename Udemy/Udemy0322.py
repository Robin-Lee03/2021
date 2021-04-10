from PIL import Image
import os

# image_file = Image.open('gray.jpg')
# image_gray = image_file.convert('L')    # 把圖片轉換成灰階
# image_file.show()
# image_gray.show()

for file in os.listdir('.'):      # 查詢此資料夾內所有的檔案
    print(file)
