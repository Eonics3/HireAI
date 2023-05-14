# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

def convert():
    openai.api_key = "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"

    # prompt = """
    # Please transcribe the following audio file:

    # include filler words and punctuation.
    # """

    audio_file= open("./test_file.mp4", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    f = open('transcript.txt', 'w')
    f.write(transcript.get("text"))
    f.close()