# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from config import OPENAI_API_KEY

def generate_questions():
    openai.api_key = OPENAI_API_KEY

    f1 = open('job_info.txt', 'r')
    job_info = f1.readlines()
    f1.close()

    f2 = open('resume.txt', 'r')
    resume = f2.readlines()
    f2.close()

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "Generate three interview questions for a %s. Here is the \
    interviewee's resume: %s. Use their resume to give THREE interview questions. \
    Generate a list of questions separated by newlines." % (job_info, resume)},
            {"role": "user", "content": "Generate THREE practice interview questions. Format them without bullet points."},
        ]
    )

    response_message = response['choices'][0]['message']['content']
    f3 = open('questions.txt', 'w')
    f3.write(response_message)
    f3.close()