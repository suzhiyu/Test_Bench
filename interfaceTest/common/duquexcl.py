#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:wuya


import  os
import  xlrd
import  json


class Helper(object):
   '''公共方法'''

   def base_dir(self,filePath,folder='data'):
      '''
      返回公共路径
      :parameter folder:文件夹
      :parameter filePath:文件名称
      '''
      return os.path.join(
         os.path.dirname(
            os.path.dirname(__file__)),
         folder,filePath)

   def readExcel(self,rowx,filePath='data.xlsx'):
      '''
      读取excel中数据并且返回
      :parameter filePath:xlsx文件名称
      :parameter rowx:在excel中的行数
      '''
      book=xlrd.open_workbook(self.base_dir(filePath))
      sheet=book.sheet_by_index(0)
      return sheet.row_values(rowx)

   def getUrl(self,rowx):
      '''
      获取请求地址
      :parameter rowx:在excel中的行数
      '''
      return self.readExcel(rowx)[1]

   def getData(self,rowx):
      '''
      获取数据并且返回
      :parameter rowx:在excel中的行数
      '''
      return  json.loads(self.readExcel(rowx)[2])




