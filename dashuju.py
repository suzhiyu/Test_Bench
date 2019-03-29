#coding=utf-8
import json

def Basic_User_Info(filename):
    file=filename

    with open(file,'r')  as load_f:
        loads_dict=json.load(load_f)
        #用户id
        print(loads_dict["_id"])
        #开户时间
        open_time = print(loads_dict["_source"]["body"]["open_time"])
        #开户姓名
        print(loads_dict["_source"]["body"]["name"])
        #身份证
        print(loads_dict["_source"]["body"]["idcard"])
        #code状态码
        print(loads_dict["_source"]["body"]["code"])
        #手机号码mobile
        print(loads_dict["_source"]["body"]["mobile"])
        #用户地址
        print(loads_dict["_source"]["body"]["address"])
        #用户入网时长
        last_modify_time=print(loads_dict["_source"]["body"]["last_modify_time"])
        #print((last_modify_time-open_time).days)
        #号码归属地省份
        province=loads_dict["_source"]["body"]["province"]
        #号码归属地市
        city=loads_dict["_source"]["body"]["city"]

#####基础数据##########

        #通话
        calls=loads_dict["_source"]["body"]["calls"]
        print(len(calls))


        #近一天通话时长
        oneday=print('通话时长',calls[0]["items"][0]["duration"])


        #通过归属地
        location=print(calls[0]["items"][0]['location'])

        # print(len(items))
        items0 = calls[0]["items"][0]
        print(len(calls[0]["items"][0]))
        #if location==city:

 #获取items数据
        print(type(calls))
        count=0
        #items=calls[0]["items"]
        #获取所有calls
        print('callslens',len(calls))
        for call_list in calls:
            #print(call_list)
            #每个calls 的items
            call_list_items=call_list["items"]
            #print(type(call_list_items))
            #一共有多少数据
            #print(len(call_list_items))
            for value in call_list_items:
                #print("输出值",value)
                #print(city)
                #print(province)
                #print('location',value.get("location"))
                if value.get("dial_type")=='DIAL' and value.get("location")  in  (city,province):
                    count=count+1

                else:
                    pass

        print(count)

        load_f.close()


if __name__ == '__main__':
    Basic_User_Info('dashuju.txt')