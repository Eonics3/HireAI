import openai
from config import OPENAI_API_KEY

def evaluate_content():
    f = open("transcript.txt", 'r')
    transcript = f.readlines()

    openai.api_key = OPENAI_API_KEY

    f2 = open('resume.txt', 'r')
    resume = f2.readlines()

    f3 = open('questions.txt', 'r')
    questions = f3.readlines()

    f4 = open('job_info.txt', 'r')
    job_info = f4.readlines()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Give feedback on how users can improve their interviewing skills for a software engineer internship at %s. Write the feedback without using first-person perspective." % job_info},
            {"role": "user", "content": "Here's my resume: %s. Here is my transcript %s. Please list constructive and concise feedback on my interview responses to the following questions: %s." % (resume, transcript, questions)},
        ]
    )

    response = response['choices'][0]['message']['content']
    print(response)