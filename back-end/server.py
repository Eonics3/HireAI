from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='../front-end', static_folder='../front-end/assets')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        resume = request.files['resume']
        video = request.files['video']
        # Save resume and mp4 to database or file system
        return jsonify({'message': [company,position]})

if __name__=='__main__':
    app.run(debug=True)