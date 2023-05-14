# Example filename: deepgram_test.py

from deepgram import Deepgram
import asyncio, json

# Your Deepgram API Key
DEEPGRAM_API_KEY = 'b2bfc931a39b7449ececd1d3e01912efcfc41c59'

# Location of the file you want to transcribe. Should include filename and extension.
# Example of a local file: ../../Audio/life-moves-pretty-fast.wav
# Example of a remote file: https://static.deepgram.com/examples/interview_speech-analytics.wav
FILE = './test_file.mp4'

# Mimetype for the file you want to transcribe
# Include this line only if transcribing a local file
# Example: audio/wav
MIMETYPE = 'mp4'

async def main():

    # Initialize the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    # Check whether requested file is local or remote, and prepare source
    if FILE.startswith('http'):
        # file is remote
        # Set the source
        source = {
        'url': FILE
        }
    else:
        # file is local
        # Open the audio file
        audio = open(FILE, 'rb')

        # Set the source
        source = {
        'buffer': audio,
        'mimetype': MIMETYPE
        }

    # Send the audio to Deepgram and get the response
    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
        source,
        {
            'punctuate': True,
            'model': 'nova',
        }
        )
    )

    # Write the response to the console
    #   print(json.dumps(response, indent=4))

    # Write only the transcript to the console
    f = open('transcript.txt', 'w')
    f.write(response["results"]["channels"][0]["alternatives"][0]["transcript"])

    # try:
    # # If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
    # #await main()
    #     asyncio.run(main())
    # except Exception as e:
    #     exception_type, exception_object, exception_traceback = sys.exc_info()
    #     line_number = exception_traceback.tb_lineno
    #     print(f'line {line_number}: {exception_type} - {e}')