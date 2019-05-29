__author__ = 'helijian'
import random
def create_name():
    userName=random.choice(['何','陈','李','张','黄','杨','百里','东方','南宫','公孙','黄甫','欧阳','端木','西门','诸葛','独孤'])+"".\
    join(random.choice("澄邈德泽海超海阳荣逸昌瀚钰瀚文涵亮涵煦涵蓄涵衍皛浩波博浩初浩浩广浩邈浩气浩思浩言鸿宝鸿波鸿博鸿才鸿畅鸿"
                       "畴鸿达鸿德鸿飞鸿风鸿福鸿光鸿晖鸿朗鸿文鸿轩鸿煊鸿骞鸿远鸿云鸿哲鸿祯鸿志鸿卓嘉澍光济澎湃彭泽鹏池鹏海浦和浦泽瑞渊越泽博耘运"
                       "宇皓钊铭锟阳韦良沛晨轩晨涛晨濡晨潍鸿振吉星铭晨起凡运凯鹏浩诚良澄邈晨浩李三云志飞轩"
                       "辕东南西北东方欧阳城北西汉唐宋元明清") for i in range(1))
    print("用户名(信息):"+userName+"\n")
    # with open("name.txt",mode="w")as f:
    #     f.write(userName)
    return userName

#
# if __name__ == '__main__':
#     name=create_name()
#     print(name)