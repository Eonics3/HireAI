import speech_to_text
import generate_questions
import evaluate
import resume_reader

def p1():
    resume_reader.readResume()
    generate_questions.generate_questions()

def p2():
    speech_to_text.convert()
    evaluate.evaluate()
