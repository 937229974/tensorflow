from train import crack_captcha_cnn
from train import  MAX_CAPTCHA,CHAR_SET_LEN,keep_prob,X
from train import  vec2text,convert2gray
from PIL import Image
import numpy as np
import tensorflow as tf
import glob,random




def predict_result(captcha_image):

    output = crack_captcha_cnn()

    saver = tf.train.Saver()
    # tf.reset_default_graph()

    with tf.Session() as sess:
        saver.restore(sess, "F:/CNN_2/model_3/crack_capcha.model-2000")
        predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)

        text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})
        # text_list = sess.run(predict, feed_dict={X: [captcha_image]})

        text = text_list[0].tolist()
        vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
        i = 0
        for n in text:
            vector[i * CHAR_SET_LEN + n] = 1
            i += 1
        return vec2text(vector)


def get_name_and_image():
    list1 = glob.glob(r"C:\Users\Administrator\Desktop\text\text\*.png")
    num  =random.randint(0,len(list1)-1)

    path = list1[num]
    print(path)
    p, image_text = path.split('_')
    captcha_text, type = image_text.split('.')

    captcha_image = Image.open(path)

    captcha_image = np.array(captcha_image)

    image = convert2gray(captcha_image)
    image = image.flatten() / 255

    return captcha_text, image
if __name__ =="__main__":
    text , image =get_name_and_image()
    predict_text = predict_result(image)
    print("正确: {}  预测: {}".format(text, predict_text))

