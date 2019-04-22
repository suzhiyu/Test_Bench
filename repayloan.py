# -*- coding: utf-8 -*-
from flask import jsonify
from flask import Flask
from flask import request
from flask import render_template
import random
import math
from suanfa import huankuanjisuan


app = Flask(__name__)

@app.route('/',methods=['GET','POSt'])
def home():
    return '<h1>Home</h1>'

@app.route('/home',methods=['GET','POSt'])
def calculator():
    return render_template("home.html")

@app.route('/zhoubao',methods=['GET'])
def zhoubao():
    return render_template("zhoubao.html")

@app.route('/zhoubaojieguo',methods=['GET'])
def zhoubaojieguo():
    zuruan = ('苏志宇', '何立建', '苟警卫', '张乃平', '丁娜', '黄香梅')
    diyizhou = random.choice(zuruan)
    dierzhou = random.choice(zuruan)
    disanzhou = random.choice(zuruan)
    disizhou = random.choice(zuruan)


    return render_template("zhoubaojieguo.html",diyizhou=diyizhou,dierzhou=dierzhou,disanzhou=disanzhou,disizhou=disizhou)



@app.route('/huankuan',methods=['GET'])
def shouye():
    return render_template('huoqushuju.html')



@app.route('/huankuan',methods=['POST'])
def jisuan():
    parame=request.form.to_dict

    jiekuanbenjin=int(request.form['jiekuanbenjin'])
    jiekuanlilv=float(request.form['jiekuanlilv'])
    jiekuanqixian=int(request.form['jiekuanqixian'])
    faxirililv=int(request.form['faxirililv'])
    yuqitianshu=int(request.form['yuqitianshu'])
    fuwufeilv=int(request.form['fuwufeilv'])


    if jiekuanbenjin  in (0,None):
        return '<h3>Bad request借款本金不能输入零或空</h3>'
    elif  jiekuanlilv  in (0,None):
        return '<h3>Bad request借款本金不能输入零或空</h3>'
    elif jiekuanqixian  in (0,None):
        return '<h3>Bad request借款本金不能输入零或空</h3>'
    elif faxirililv in (0,None):
        return '<h3>Bad request借款本金不能输入零或空</h3>'
    elif fuwufeilv  in (0,None):
        return '<h3>Bad request借款本金不能输入零或空</h3>'
    else:

        lixi= round(jiekuanlilv/100/360*jiekuanqixian*jiekuanbenjin,2)
        print(lixi)
        faxi=round(jiekuanlilv*faxirililv*yuqitianshu,2)
        print(faxi)
        fuwufei=jiekuanbenjin*fuwufeilv/100
        print(fuwufeilv)
        zonghuankuanjine=jiekuanbenjin+lixi+faxi
        print(['总还款金额', jiekuanbenjin + lixi + faxi], ['利息', lixi], ['罚息', faxi], ['服务费，放款直接扣', fuwufei])
        return  render_template('jieguo.html',lixi=lixi,faxi=faxi,fuwufei=fuwufei,zonghuankuanjine=zonghuankuanjine,jiekuanbenjin=jiekuanbenjin,jiekuanlilv=jiekuanlilv,jiekuanqixian=jiekuanqixian,faxirililv=faxirililv,yuqitianshu=yuqitianshu,fuwufeilv=fuwufeilv)
    if 'expression' not in parame:
        return jsonify({
            'status': 400,
            'message': 'miss parameter [expression]',
            'data': parame
        })
    try:
        result = eval(parame['expression'])

        return jsonify({
            'status': 0,
            'message': 'success',
            'data': result
        })
    except SyntaxError:
        return jsonify({
            'status': 500,
            'message': 'invalid expression',
            'data': parame['expression']
        })


# parame = request.form.to_dict
@app.route('/huankuanjisuan', methods=['POST'])
def fangfajisuan():
    loanamount = int(request.form['loanamount'])
    print('++++++', loanamount)
    rate = float(request.form['rate'])
    print(rate)
    periods = int(request.form['periods'])
    print(periods)
    gongshi = str(request.form['gongshi'])
    print(gongshi)

    if gongshi == 'dengebenxi':
        meiqihuankuane =huankuanjisuan.dengebenxi(loanamount, rate, periods)["meiqihuankuane"]
        huankuanzonge=huankuanjisuan.dengebenxi(loanamount, rate, periods)["huankuanzonge"]
        return render_template('suanfajieguo.html',meiqihuankuane=meiqihuankuane,huankuanzonge=huankuanzonge,loanamount=loanamount,rate=rate,periods=periods,gongshi=gongshi)
    elif gongshi == 'dengbendengxi':
        meiqihuankuane=huankuanjisuan.dengbendengxi(loanamount,rate,periods)["meiqihuankuane"]
        huankuanzonge=huankuanjisuan.dengbendengxi(loanamount,rate,periods)["huankuanzonge"]
        return render_template('suanfajieguo.html',meiqihuankuane=meiqihuankuane,huankuanzonge=huankuanzonge,loanamount=loanamount,rate=rate,periods=periods,gongshi=gongshi)
    else:
        return '<h3>Bad requests算法输入错误，请重新输入</h3>'




    if 'expression' not in parame:
        return jsonify({
            'status': 400,
            'message': 'miss parameter [expression]',
            'data': parame
        })
    try:
        result = eval(parame['expression'])

        return jsonify({
            'status': 0,
            'message': 'success',
            'data': result
        })
    except SyntaxError:
        return jsonify({
            'status': 500,
            'message': 'invalid expression',
            'data': parame['expression']
        })



class MyException(Exception):
        def __init__(self, message):
            Exception.__init__(self)
            self.message = message


if __name__ == '__main__':
    app.run(host='192.168.37.25',
            port='9001',
            debug=True)
