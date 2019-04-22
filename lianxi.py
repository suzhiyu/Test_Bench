#coding=utf-8
#贷款总额loanamount，借款利率rate 、借款期数periods
import math
#借款本金
#借款利息
#借款月利率
#借款期限

#等额本息算法每期还款本息和公式：
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
        return meiqihuankuane,huankuanzonge
    def dengbendengxi(loanamount,rate,periods):
        #月利率
        rates=rate/12/100
        #每期还款金额=本金*（1+年利率)/总期数
        meiqihuankuane1=round(loanamount*rates+loanamount/periods,2)
        #print(meiqihuankuane1)
        #print(round(meiqihuankuane1*periods,2))

        huankuanzonge1=round(loanamount*rates*periods+loanamount,2)
        #print(huankuanzonge1)
        print(meiqihuankuane1, huankuanzonge1)
        return meiqihuankuane1,huankuanzonge1

    def huankuanjisuan(loanamount,rate,periods,gongshi):

        if gongshi == 'dengebenxi':
                return huankuanjisuan.dengebenxi(loanamount, rate, periods)
        elif gongshi == 'dengbendengxi':
                return  huankuanjisuan.dengbendengxi(loanamount, rate, periods)
        else:
            return print("++算法输入错误+++")


if __name__ == '__main__':
    aa=huankuanjisuan
    aa.huankuanjisuan(5000,36,3,"dengbendengxi")

