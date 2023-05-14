# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

def evaluate():
    f = open("transcript.txt", 'r')
    transcript = f.readlines()

    openai.api_key = "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"

    f2 = open('resume.txt', 'r')
    resume = f2.readlines()

    f3 = open('questions.txt', 'r')
    questions = f3.readlines()

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are giving feedback on how users can improve their interviewing skills for a software engineer internship. Write the feedback without using first-person perspective."},
            {"role": "user", "content": "Here's my resume: %s. Here is my transcript %s. Please give constructive and concise feedback on my \
    interview responses to the following questions: %s" % (resume, transcript, questions)},
        ]
    )

    response_message = response['choices'][0]['message']['content']
    print(response_message)