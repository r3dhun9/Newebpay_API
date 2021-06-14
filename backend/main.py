from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from utils.Crypto import *
import time
import templates

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    data = {
        "MerchantID": "MS120725784",
        "RespondType": "JSON",
        "TimeStamp": str(int(time.time())),
        "Version": "1.6",
        "MerchantOrderNo": "S_" + str(int(time.time())),
        "LoginType": "0",
        "Amt": "10000",
        "ItemDesc": "【一定好看】77歲富豪娶嫩妻-須藤早貴三個月後離奇暴斃",
        "Email": "redhung@hung.red",
    }
    parse_data = gen_query_string(data)
    trade_info = create_mpg_aes_encrypt(parse_data.encode())
    trade_sha = create_mpg_sha_encrypt(trade_info)
    return render_template("index.html", trade_info=trade_info, trade_sha=trade_sha)

@app.route("/checkout", methods=['POST'])
def checkout():
    post_data = request.json
    product_name = post_data['productName']
    product_price = post_data['productPrice']
    product_quantity = post_data['productQuantity']
    customer_name = post_data['customerName']
    customer_email = post_data['customerEmail']
    customer_phone = post_data['customerPhone']
    
    trade_data = {
        "MerchantID": "MS120725784",
        "RespondType": "JSON",
        "TimeStamp": str(int(time.time())),
        "Version": "1.6",
        "MerchantOrderNo": "S_" + str(int(time.time())),
        "LoginType": "0",
        "Amt": product_price,
        "ItemDesc": product_name,
        "Email": customer_email,
    }

    parse_data = gen_query_string(trade_data)
    trade_info = create_mpg_aes_encrypt(parse_data.encode())
    trade_sha = create_mpg_sha_encrypt(trade_info)

    return jsonify({"tradeInfo": trade_info, "tradeSha": trade_sha})

if __name__ == "__main__":
    app.run(port = 8888)