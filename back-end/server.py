from flask import Flask, render_template, request, jsonify
import os

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

        # Combine company and position into a single string
        job_info = company + ' ' + position
        
        # Save job_info to a text file
        file_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'job_info.txt')
        with open(file_path, 'w') as file:
            file.write(job_info)

        # Save resume to a pdf file
        resume.save(os.path.join(os.pardir, 'models', 'resume.pdf'))

        # Save resume and mp4 to database or file system
        return jsonify({'message': [company,position]})

if __name__=='__main__':
    app.run(debug=True) 