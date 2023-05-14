from flask import Flask, render_template, request, redirect, send_from_directory
import os
# import main.py from "../models/main.py"
# import os
import sys

# script_dir = os.path.dirname( __file__ )
# mymodule_dir = os.path.join( script_dir, '..', 'models')
# sys.path.append( mymodule_dir )
import main

app = Flask(__name__, template_folder='../front-end')
app.static_folder = '../front-end/assets'

# Define the path to the vendor folder
vendor_path = '../front-end/vendor'

# Serve the feedback.html file from the static_folder
@app.route('/feedback.html')
def serve_feedback():
    return send_from_directory(app.static_folder, 'feedback.html')

# Serve files from the vendor folder
@app.route('/vendor/<path:filename>')
def serve_vendor_file(filename):
    return send_from_directory(vendor_path, filename)

# Add all the JS files from the js folder to the static_folder for feedback.html
@app.route('/js/<path:filename>')
def serve_js_file(filename):
    return send_from_directory('../front-end/js', filename)

# Add all the CSS files from the css folder to the static_folder for feedback.html
@app.route('/css/<path:filename>')
def serve_css_file(filename):
    return send_from_directory('../front-end/css', filename)

# Add all the CSS files from the css folder to the static_folder for feedback.html
@app.route('/img/<path:filename>')
def serve_img_file(filename):
    return send_from_directory('../front-end/img', filename)

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
    main.p2()


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
    l1 = q1_line[0]
    l2 = q2_line[0]
    l3 = q3_line[0]

    q1 = '\n'.join(q1_line[-4:])
    q2 = '\n'.join(q2_line[-4:])
    q3 = '\n'.join(q3_line[-4:])

    filler_num = float(filler_num_file.readline())
    sentiment = float(sentiment_file.readline())

    return render_template('feedback.html',l1=l1,l2=l2,l3=l3,q1=q1,q2=q2,q3=q3, filler_num=filler_num, sentiment=sentiment)

if __name__=='__main__':
    app.run(debug=True) 