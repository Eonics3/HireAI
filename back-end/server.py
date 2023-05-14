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
def uploadQuestions():
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

        main.p1()

        # Save resume and mp4 to database or file system
        return redirect(f'/questions')

@app.route('/questions')
def questions():
    f = open('questions.txt', 'r')
    questions = f.readlines()

    return render_template('questions.html',q1=questions[0],q2=questions[1],q3=questions[2])

@app.route('/questions', methods=['POST'])
def uploadVideo():
    video = request.files['video']
    video.save('video.mp4')

    return redirect(f'/feedback')

@app.route('/feedback')
def feedback():
    with open("question1.txt", 'r') as file:
        q1_line = file.readlines()
    with open("question2.txt", 'r') as file:
        q2_line = file.readlines()
    with open("question3.txt", 'r') as file:
        q3_line = file.readlines()
    filler_num_file = open('filler_num.txt', 'r')
    sentiment_file = open('sentiment.txt', 'r')

    last_1lines = q1_line[-4:]
    last_2lines = q2_line[-4:]
    last_3lines = q3_line[-4:]

    q1 = ''.join(last_1lines)
    q2 = ''.join(last_2lines)
    q3 = ''.join(last_3lines)

    filler_num = float(filler_num_file.readline())
    sentiment = float(sentiment_file.readline())

    return render_template('feedback.html',q1=q1,q2=q2,q3=q3, filler_num=filler_num, sentiment=sentiment)

if __name__=='__main__':
    app.run(debug=True) 