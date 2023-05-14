from flask import Flask, render_template, request, redirect, jsonify
import os
# import main.py from "../models/main.py"
# import os
import sys

# script_dir = os.path.dirname( __file__ )
# mymodule_dir = os.path.join( script_dir, '..', 'models')
# sys.path.append( mymodule_dir )
import main

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
        file_path = os.path.join('job_info.txt')
        with open(file_path, 'w') as file:
            file.write(job_info)

        # Save resume to a pdf file
        resume.save('resume.pdf')

        print("running main()... ")

        main.p1()

        # Save resume and mp4 to database or file system
        return redirect(f'/questions')

@app.route('/questions')
def questions():
    f = open('questions.txt', 'r')
    questions = f.readlines()

    return render_template('questions.html',q1=questions[0],q2=questions[1],q3=questions[2])


if __name__=='__main__':
    app.run(debug=True) 