__author__ = 'helijian'
import random

def create_mobile():
    mobile = random.choice(['144', '155', '166' ]) + "".join(random.choice("0123456789") for i in range(8))
    #print('')
    # with open("mobile.txt", mode="w")as f:
    #     print("手机号(信息)："+mobile+"\n")
    #     f.write(mobile)
    return mobile
