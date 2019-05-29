#coding: utf-8
'''
unittest merchant backgroud interface
@author: zhiyu su
@version: 1.0
'''
import requests
import unittest
import json
import traceback
import time
import pandas

def readTestCase(testCaseFile):
	testCases = pandas.read_excel(testCaseFile)
	return testCases

def getJsonPayload(testCases):
	testCases['payload'] = testCases['payload'].apply(json.loads)
	return testCases['payload']





class MytestSuite(unittest.TestCase):


    def setUp(self):
        print("starting...")

        self.base_url="http://preview.airwallex.com:30001/bank"
    def payload(self):


        #url
        #获取变量
        #接口请求参数
        querystring = {
	"payment_method": "SWIFT",
	"bank_country_code": "US",
	"account_name": "John Smith",
	"account_number": "123",
	"swift_code": "ICBCUSBJ",
	"aba": "11122233A"
}

        #请求头部
        headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }
       # try:
        #post 请求
        response = requests.request("POST", url=self.base_url, headers=headers,json=querystring)
        r=requests.pos

        #对http 返回值进行判断，对于200的做基本校验
        if response.status_code==200:
            response.encoding=response.apparent_encoding
            results=json.loads(response.text)
            result=results["return_code"]
            #print(result)

            self.assertIsNot(result,000000,msg='两个值不相等')
        else:
            raise Exception("http error info ",response.status_code)



    def tearDown(self):
        print("close...")
       # except :
   # traceback.print_exc()

#执行case
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(MytestSuite("payload"))

    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

