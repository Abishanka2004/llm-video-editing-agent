import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import whisper
import subprocess
from config import FINAL_OUTPUT

model = whisper.load_model("tiny", device="cpu")


def generate_subtitles(input_video):

    print("Transcribing audio...")

    result = model.transcribe(input_video)

    segments = result["segments"]

    srt_file = "output/subtitles.srt"

    # Create SRT file
    with open(srt_file, "w", encoding="utf-8") as f:

        for i, segment in enumerate(segments, start=1):

            start = format_time(segment['start'])
            end = format_time(segment['end'])
            text = segment['text']

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")

    print("Subtitles file created")

    # Burn subtitles into video using FFmpeg
    cmd = f'ffmpeg -y -i "{input_video}" -vf subtitles="{srt_file}" "{FINAL_OUTPUT}"'

    subprocess.run(cmd, shell=True)

    print("Final video created")

    return FINAL_OUTPUT


def format_time(seconds):

    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"
