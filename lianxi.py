from flask import jsonify
from flask import Flask
import requests
from flask import render_template

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/yunyingshangmock",methods=["GET"])

def mockhtml():

    return render_template("yunyingshangmock.html")


@app.route("/yunyingshangmockcallback",methods=["post"])



def yunyingshangmockcallback():


    #req=requests.post()


    return jsonify({"status":"成功"})

def yunyingshangmockreport():

    return



if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port='9898',
            debug=True)






