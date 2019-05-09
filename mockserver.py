#coding:utf-8
from flask import abort, jsonify, Flask, request, Response
import json

app=Flask(__name__)
# 不需要转译#解决返回乱码
app.config['JSON_AS_ASCII'] = False

# @app.route("/mockserver",methods=['get'])
# def get_back_res():
#     return jsonify(response)
#
#
#
# @app.route("/mockserver",methods=['post'])
# def post_back_res():
#     return jsonify(response)
#
# response={
# 	"body": {
# 		"code": "200",
# 		"data": {
# 			"extend": "-1",
# 			"tags": "md000"
# 		},
# 		"requestId": "9DA1960B-4D3D-4D73-B70C-C2D0B5A242DE",
# 		"message": "OK"
# 	},
# 	"message": {
# 		"desc": "成功",
# 		"status": "000000"
# 	}
# }
# response={
#  	"body": {
#  		"code": "200",
#  		"data": {
#  			"extend": "-1",
#  			"tags": "md000"
#  		},
#  		"requestId": "9DA1960B-4D3D-4D73-B70C-C2D0B5A242DE",
#  		"message": "OK"
#  	},
#  	"message": {
#  		"desc": "成功",
#  		"status": "000000"
#  	}
#  }


@app.route("/mockserver",methods=["GET","POST"])
def api_call_back():
	response = {
		"body": {
			"code": "200",
			"data": {
				"extend": "-1",
				"tags": "md000"
			},
			"requestId": "9DA1960B-4D3D-4D73-B70C-C2D0B5A242DE",
			"message": "OK"
		},
		"message": {
			"desc": "成功",
			"status": "000000"
		}
	}

	if request.method=='GET':
		return jsonify("response")
	else:
		#get_json 直接转化为json
		#get_data 获取出来的是对象 需要做json 转化           json_data=json.loads(test_data)
		#下面屏蔽的是获取对象，之后利用json。loads 转换成标准json数据
		#test_data=request.get_data()
		#json_data=json.loads(test_data)
		test_data=request.get_json()
		print(test_data)
		return jsonify(test_data)




if __name__ == "__main__":
	#运行flask 指定ip 端口
	app.run(host="192.168.37.25",
			port=8989,
			debug=True)