#coding: utf-8
'''
unittest merchant backgroud interface
@author: zhang_jin
@version: 1.0
@see:http://www.python-requests.org/en/master/
'''
import requests
import unittest
import json
import traceback
import unittest
import time
import  interfaceTest.common.Sj_mobile
import  interfaceTest.common.Sj_name
import interfaceTest.common.Sj_sfz
import random

class MytestSuite(unittest.TestCase):
    def setUp(self):
        print("starting...")
    def zhucejiekou_001(self):


        #url
        url = "http://sit-customer.dzjk.infra/customerMng/customerEasyRegister"
        #获取变量
        realName=interfaceTest.common.Sj_name.create_name()
        mobile=interfaceTest.common.Sj_mobile.create_mobile()
        area_code = random.choice(["340322", "140226"])
        idNum=interfaceTest.common.Sj_sfz.gen_id_card(int(area_code), 22, 1)
        #接口请求参数
        querystring = {
        "idNum": idNum,
           "realName": realName,
           "mobile": "mobile",
           "clientType": "h5",
           "ip": "172.0.0.1"
           }

        #请求头部
        headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }
       # try:
        #post 请求
        response = requests.request("POST", url, headers=headers,json=querystring)

        #对http 返回值进行判断，对于200的做基本校验
        if response.status_code==200:
            response.encoding=response.apparent_encoding
            results=json.loads(response.text)
            result=results["return_code"]
            #print(result)

            self.assertIsNot(result,1,msg='两个值不相等')
        else:
            raise Exception("http error info ",response.status_code)



    def tearDown(self):
        print("close...")
       # except :
   # traceback.print_exc()

#执行case
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(MytestSuite("zhucejiekou_001"))

    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

