import openai
from config import OPENAI_API_KEY

def parse_questions(response):
    print("in parse_questions...")

    question_num = 1  # Initialize the question number

    lines = response.splitlines()

    for line in lines:
        if line.strip().startswith("Question"):
            new_file = open('question%d.txt' % question_num, 'w')
            new_file.write(line.strip() + "\n")
            question_num += 1
        elif line.strip() != "":
            new_file.write(line + "\n")

        # new_file.close()  # Close the file after writing to it

def evaluate_content():
    f = open("transcript.txt", 'r')
    transcript = f.readlines()[0].strip()

    openai.api_key = OPENAI_API_KEY

    f2 = open('resume.txt', 'r')
    resume = f2.readlines()[0].strip()

    f3 = open('questions.txt', 'r')
    questions = f3.readlines()[0].strip()

    f4 = open('job_info.txt', 'r')
    job_info = f4.readlines()[0].strip()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=.3,
        messages=[
            {"role": "system", "content": "Give feedback on how users can improve their interviewing skills for a software engineer internship at %s for each of the THREE questions. Write the feedback without using first-person perspective. \
             Format your answers like: Question 1: ... [Feedback for question 1.] Question 2: ... [Feedback for question 2.] Question 3: ... [Feedback\
              for questions 3.]" % job_info},
            {"role": "user", "content": "Here's my resume: %s. Here is my transcript %s. List 3 sentences of feedback for my interview responses to each of the THREE following questions: %s. I would like separated feedback for each of the three questions." % (resume, transcript, questions)},
        ]
    )

    response = response['choices'][0]['message']['content']
    # parse the last sentence from output to find score.

    parse_questions(response)