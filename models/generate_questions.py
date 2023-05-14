# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

def generate_questions():
    openai.api_key = "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"

    f1 = open('job_info.txt', 'r')
    job_info = f1.readlines()
    f1.close()

    f2 = open('resume.txt', 'r')
    resume = f2.readlines()
    f2.close()

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are generating practice interview questions for interested software engineering interviewees at %s. Here is the \
    interviewees resume: %s. Please use their resume to give 2 short and simple resume-related questions and one behavioral question. \
    Generate a list of questions separated by newlines." % (job_info, resume)},
            {"role": "user", "content": "Generate 3 practice interview questions."},
        ]
    )

    response_message = response['choices'][0]['message']['content']
    f3 = open('questions.txt', 'w')
    f3.write(response_message)
    f3.close()