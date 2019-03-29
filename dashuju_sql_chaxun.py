#coding=utf-8
import pymysql
import sql_config

# Python的DB-API，为大多数的数据库实现了接口，使用它连接各数据库后，就可以用相同的方式操作各数据库。
#
# Python DB-API使用流程：
#
# 引入 API 模块。
# 获取与数据库的连接。
# 执行SQL语句和存储过程。
# 关闭数据库连接。

host='172.16.80.31'
user='tmp_s'
password='KWcOlVpdGjap1gc1'
port=1336
# sql="SELECT callout_duration_180days,callout_counts_180days,callout_unique_numbers_180days,mobile_callout_duration_180days,mobile_callout_counts_180days,mobile_callout_unique_numbers_180days,callin_duration_180days,callin_counts_180days,callin_unique_numbers_180days,mobile_callin_duration_180days,mobile_callin_counts_180days,mobile_callin_unique_numbers_180days,midnight_call_counts_180days,midnight_call_duration_180days,midnight_call_unique_numbers_180days,midnight_mobile_call_duration_180days,midnight_mobile_call_counts_180days,midnight_mobile_call_unique_numbers_180days from dmp.moxie_carrier_ex_data_credit_180_days where orgreqno='086088a5-a2f1-4392-bfe3-31e3d7566ff3';"
# sql2="SELECT callout_duration_90days,callout_counts_90days,callout_unique_numbers_90days,mobile_callout_duration_90days,mobile_callout_counts_90days,mobile_callout_unique_numbers_90days,callin_duration_90days,callin_counts_90days,callin_unique_numbers_90days,mobile_callin_duration_90days,mobile_callin_counts_90days,mobile_callin_unique_numbers_90days,midnight_call_counts_90days,midnight_call_duration_90days,midnight_call_unique_numbers_90days,midnight_mobile_call_duration_90days,midnight_mobile_call_counts_90days,midnight_mobile_call_unique_numbers_90days from dmp.moxie_carrier_ex_data_credit_90_days where orgreqno='086088a5-a2f1-4392-bfe3-31e3d7566ff3';"



def chaxun_sql(host,user,password,pord):

    # 打开数据库连接

    db=pymysql.connect(host=host,user=user,password=password,port=port)
    print('连接成功')
    # 使用 cursor() 方法创建一个游标对象 cursor
    orgreqnocursor=db.cursor()
    cursor = db.cursor()
    cursor1=db.cursor()

    # 使用 execute()  方法执行 SQL 查询

    orgreqnosql="SELECT orgreqno from dmp.moxie_carrier_ex_data_base ;"
    orgreqnocursor.execute(orgreqnosql)
    results_orgreqno=orgreqnocursor.fetchall()
    #print(type(results_orgreqno))

    for orgreqno in results_orgreqno:
        orgreqno1=orgreqno[0]


        sql = "SELECT * from dmp.moxie_carrier_ex_data_credit_180_days where orgreqno='{}';".format(orgreqno1)
        #print(sql)
        sql2 = "SELECT * from dmp.moxie_carrier_ex_data_credit_90_days where orgreqno='{}';".format(orgreqno1)

        cursor.execute(sql)
        cursor1.execute(sql2)

    #获取全部数据
        results=cursor.fetchone()
    #print('180天',results)
    #print(len(results))
    #print('180天截取',results[1:80])
    #print(len(results[1:80]))
        shuzu=results[1:74]

        results2 = cursor1.fetchone()
    #print('90天',results2)
    #print(len(results2))
        #results2[1:80]
    #print('90天截取', results2[1:80])
    #print(len(results2[1:80]))
        shuzu2=results2[1:74]

        for i in range(len(shuzu)):

            if float(shuzu[i]) < float(shuzu2[i]):
                print(shuzu[i], shuzu2[i])
                print(orgreqno1)
                shuzu_chuli=float(shuzu[i])
                shuzu2_chuli=float(shuzu2[i])
                print(type(shuzu_chuli, shuzu2_chuli))
                print('chucuo')
            else:
                pass

        shuzubilv=results[74:80]
        shuzu2bilv=results2[74:80]
        for a in range(len(shuzubilv)):
            if float(shuzubilv[a])<float(shuzu2bilv[a]):
                print(shuzubilv[a],shuzu2bilv[a])
                print(orgreqno1)
                print("出错")

                break
            else:
                pass


    cursor.close()
    print('链接关闭')
    cursor1.close()
    print('链接关闭')
    orgreqnocursor.close()
    print('链接关闭')




if __name__ == '__main__':
    chaxun_sql(host,user,password,port)