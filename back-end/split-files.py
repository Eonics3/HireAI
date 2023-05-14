from pydub import AudioSegment

file_name = "test_file.mp4"

transcript = AudioSegment.from_file(file_name, format="mp4")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

total_duration=len(transcript)

segments = range(0, total_duration, ten_minutes)

for i, start_time in enumerate(segments):
    end_time = start_time + ten_minutes
    segment = transcript[start_time:end_time]
    segment.export(f"segment_{i}.mp4", format="mp4")