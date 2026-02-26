import sys
import os
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def extract_audio(input_video):

    print("Extracting audio...")

    output_audio = "output/audio.mp3"

    cmd = f'ffmpeg -y -i "{input_video}" -q:a 0 -map a "{output_audio}"'

    subprocess.run(cmd, shell=True)

    print("Audio extraction complete")

    return output_audio
