from flask import Flask 

app = Flask(__name__)

@app.route('/members')
def members():
    return {'Members':['Member1','Member2','Member3']}

if __name__=='__main__':
    app.run(debug=True)