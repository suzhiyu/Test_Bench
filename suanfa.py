#coding=utf-8
import math
class huankuanjisuan:



    def dengebenxi(loanamount,rate,periods):
        rates = rate / 12 / 100
        # 每期还款本息和
        meiqihuankuane=round(loanamount*rates*math.pow(1+rates,periods)/(math.pow(1+rates,periods)-1),2)
        #每期还款本金


        #每期还款利息

        # 还款总金额
        huankuanzonge=round(loanamount*rates*math.pow(1+rates,periods)/(math.pow(1+rates,periods)-1)*periods,2)
        print(meiqihuankuane,huankuanzonge)
        return {"meiqihuankuane":meiqihuankuane,"huankuanzonge":huankuanzonge}
    def dengbendengxi(loanamount,rate,periods):
        #月利率
        rates=rate/12/100
        #每期还款金额=本金*（1+年利率)/总期数
        meiqihuankuane=round(loanamount*rates+loanamount/periods,2)
        #print(meiqihuankuane1)
        #print(round(meiqihuankuane1*periods,2))

        huankuanzonge=round(loanamount*rates*periods+loanamount,2)
        #print(huankuanzonge1)
        print(meiqihuankuane, huankuanzonge)
        return {"meiqihuankuane":meiqihuankuane,"huankuanzonge":huankuanzonge}
