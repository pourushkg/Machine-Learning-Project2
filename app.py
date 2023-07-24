<<<<<<< HEAD
from flask import Flask 

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine Learnig Project"

if __name__=='__main__':
=======
from flask import Flask 

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine Learnig Project"

if __name__=='__main__':
>>>>>>> 01a705bde0e466e4c7ef37fe378646dc4f6c84a2
    app.run(debug=True)