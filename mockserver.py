from flask import abort,jsonify,Flask,Request,Response


app=Flask(__name__)
@app.route("/mockserver",methods=['get'])
def get_back_res():
    return jsonify(response)



@app.route("/mockserver",methods=['post'])
def post_back_res():
    return jsonify(response)

response={
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




if __name__ == "__main__":
    app.run(
    host = "192.168.37.25",
    port = 8989,
    debug = True
        )