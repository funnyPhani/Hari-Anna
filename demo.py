from Scode import get_data as Data
from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def welcome():
    return f"Hello"
#get route
@app.route("/cook_get",methods = ['GET'])
def data_get_route():
    query = request.args.get("query")
    if not query:
        return jsonify({"error":"becuase of query is not given"})
    else:
        df = Data(query)
        return jsonify(df)
#post route
@app.route("/cook_post",methods = ["POST"])
def data_post_route():
    query = request.json["query"]
    if not query:
        return jsonify({"error":"pass data in post manner"})
    else:
        df = Data(query)
        return jsonify(df)



if __name__ == '__main__':
    app.run(debug=True)