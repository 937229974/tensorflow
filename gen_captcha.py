#coding=utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import os,glob

# 验证码中的字符, 就不用汉字了

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
'''
number=['0','1','2','3','4','5','6','7','8','9']
alphabet =[]
ALPHABET =[]
'''

# DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
# DEFAULT_FONTS = [os.path.join(DATA_DIR, 'DroidSansMono.ttf')]
#
# class ImageCaptcha(ImageCaptcha):
#
#     def __init__(self):
#         # (self, width=180, height=67, fonts=None, font_sizes=None):
#         self._width = 180
#         self._height = 67
#         self._fonts = None or DEFAULT_FONTS
#         self._font_sizes = None or (42, 50, 56)
#         self._truefonts = []
# 验证码一般都无视大小写；验证码长度4个字符
def random_captcha_text(char_set=number + alphabet + ALPHABET, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text


# 生成字符对应的验证码
def gen_captcha_text_and_image():

    while(1):
        image = ImageCaptcha(180,67)
        # image = ImageCaptcha()

        captcha_text = random_captcha_text()
        captcha_text = ''.join(captcha_text)
        path = 'F://CNN_1/test/'
        print("-----------------"+captcha_text)
        captcha = image.generate(captcha_text)
        # image.write(captcha_text, path+captcha_text + '.jpg')  # 写到文件

        captcha_image = Image.open(captcha)
        #captcha_image.show()
        captcha_image = np.array(captcha_image)
        if captcha_image.shape==(67,180,3):
            break

    return captcha_text, captcha_image


num = 1
def read_localhost_images(path1):
    global num
    list = glob.glob(path1)
    if num == len(list) :
        num = 1

    if num < len(list):
        path = list[num]
        # print(path)
        p, image_text = path.split('_')
        captcha_text, type = image_text.split('.')

        captcha_image = Image.open(path)

        captcha_image = np.array(captcha_image)
        num += 1
        # if captcha_image.shape == (67, 180, 4):
        #     break

        return captcha_text, captcha_image

def get_name_and_image():
    list = glob.glob(r"C:\Users\Administrator\Desktop\1\*.png")
    num  =random.randint(0,len(list)-1)

    path = list[num]
    # print(path)
    p, image_text = path.split('_')
    captcha_text, type = image_text.split('.')

    captcha_image = Image.open(path)

    captcha_image = np.array(captcha_image)

    return captcha_text, captcha_image

if __name__ == '__main__':
  while 1:
    # 测试
    text, image = gen_captcha_text_and_image()
    # print image
    gray = np.mean(image, -1)
    # print gray

    # print image.shape
    # print gray.shape
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(image)

    plt.show()
