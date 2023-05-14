import openai
from config import OPENAI_API_KEY

def findScore(txt):
    score = [int(s) for s in txt.split() if s.isdigit()]
    return score

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
            {"role": "system", "content": "Give feedback on how users can improve their interviewing skills for a software engineer internship at %s for each of the three questions. Write the feedback without using first-person perspective. \
             Format your answers like: Question 1: ... [Feedback for question 1.] Question 2: ... [Feedback for question 2.] Question 3: ... [Feedback\
              for questions 3.] In the last sentence of your response, write a score from 1-100, too." % job_info},
            {"role": "user", "content": "Here's my resume: %s. Here is my transcript %s. Please list around 4 sentences feedback for EACH of my interview responses to EACH of the following questions: %s." % (resume, transcript, questions)},
        ]
    )

    response = response['choices'][0]['message']['content']
    # parse the last sentence from output to find score.

    index = response.rindex('.', 0, len(response)-2)

    score = findScore(response[index:]) # string number

    print("score: ", score)

    response = response[:index]

    print(response)
    print("Score (1-100): ", score)

    # TODO: parse each response

    # response_list = 
    if len(score)==1:
        return response, score[0]
    else:
        return response, 70