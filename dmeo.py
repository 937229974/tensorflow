import glob
import random
from PIL import Image
def read_image():
    list1 =   glob.glob(r"C:\Users\Administrator\Desktop\1\*.png")

    num = random.randint(0, len(list1))
    print('------',num )
    # for href in list1:
    #     print(href)
    path = list1[1]
    p ,image_text = path.split('_')
    image_text , type = image_text.split('.')
    print(image_text)
def check_image_rule():
    list1 = glob.glob(r"C:\Users\Administrator\Desktop\1\*.png")
    for i,v in enumerate(list1):
        try:
            p, image_text = v.split('_')
            captcha_text, type = image_text.split('.')
        except:
            pass


        if v.count("_") != 1 or len(captcha_text) >4 or v.count(' ') >0 :

            print(str(i)+"-------------------"+v)

if __name__ == "__main__":
    read_image()
    # check_image_rule()
