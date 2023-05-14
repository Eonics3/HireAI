import speech_to_text_deepgram
import generate_questions
import evaluate
import resume_reader
import asyncio
import evaluate_filler

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

    

# def m(company, position, resume, video):
#     job_info = company + "\n" + position
#     resume, questions = p1(resume, job_info)
#     evaluation = p2(resume, job_info, video, questions)

#     return evaluation()

async def main():
    p1()
    await p2()

asyncio.run(main())