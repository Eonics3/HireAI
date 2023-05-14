import speech_to_text_deepgram
import generate_questions
import evaluate
import resume_reader
import asyncio
import evaluate_filler
import evaluate_sentiment

def p1():
    resume_reader.readResume()
    generate_questions.generate_questions()

async def p2():
    await speech_to_text_deepgram.main()

    evaluate.evaluate_content()
    filler, total = evaluate_filler.evaluate_filler()
    if filler/total >= 0.1:
        print("You used %d filler words during your mock interview.")
        print("Filler words like um may seem natural in everyday speech, but they do not belong in formal presentations or speeches. Next time,\
try to use less filler words such as um, like, such as... during interviews.")
        print("")
    else:
        print("You used very little filler words during your mock interview. Good job!")
    
    # figure out how to quantify filler from 0-100

    sentiment_score = evaluate_sentiment.evaluate_sentiment()
    if sentiment_score > 0.8:
        print("Great Job! Your attitude reflected positivity, a trait that is crucial for an interview.")
    elif sentiment_score > 0.6:
        print("Good Job! Your attitude was good, but could use a bit more work. Try to incorporate more enthusiastic language. Confidence is key!")
    elif sentiment_score > 0.3:
        print("Not bad, try to improve your perceived positivity next time. Hiring managers see positivity as one of the key traits they look for when interviewing interns.")
    else:
        print("Your attitude was poor. Positivity is a key trait interviewers look for, so improving your demeanor is a key area of your interview you could improve on. Here are some tips: https://www.indeed.com/career-advice/interviewing/tips-for-staying-positive-during-interview")

async def main():
    p1()
    await p2()

asyncio.run(main())