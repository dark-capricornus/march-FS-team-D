from flask import Flask,request,jsonify

app =Flask(__name__)

@app.route("/newone",methods=["POST"]) #aditional feature (decorator)
def index():
    return "welcome to our company sura",201

#DYNAMIC ROUTING 
@app.route("/add/<int:a>/<int:b>",methods=["GET"])
def add(a,b):
    result=str(a*b)
    return result,200

#routing with body 
@app.route("/search",methods=["GET"])
def search():
    payload =request.json  #routing with body u have send the information in json format
    id=request.args.get("id")#getting information from url query parameter
    name=request.args.get("name")
    message=f'the person {name} is {id} years old'
    res={
        "status":"success",
        "message" : message
    }
    return jsonify(res),200 #to response the result in the form of json format but python result in dictionary format 
 




@app.route("/teamlead",)
def mom():
    return "Have U Completed the work"

if __name__=="__main__":
    app.run(debug=True,port=3000)