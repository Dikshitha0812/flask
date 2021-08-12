from flask import Flask,jsonify,request

app=Flask(__name__)
tasks =[
    {
        'id':1,
        'title':u'Do Studies',
        'description':u'Maths And science',
        'done':False
    },
    {
        'id':2,
        'title':u'Do the Quiz',
        'description':u'Coding',
        'done':False
    }
]
@app.route('/')
def hello ():
    return "Website Working!!"
@app.route("/add-data",methods=["POST"])
def adddata():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "Message":"Please Provide The Data"
        })
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
                "Status":"Successful!",
                "Message":"Task Added Sucessfully!!"
            })
@app.route('/get-data',methods=["GET"])
def getdata():
    return jsonify({
        'data':tasks

    })


if __name__ =="__main__":
    app.run(debug=True)
