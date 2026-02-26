import sys
import os

# FIX PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.extract_audio import extract_audio
from tools.subtitles import generate_subtitles
from tools.trim import trim_video
from tools.silence_removal import remove_silence


def execute(plan, input_video):

    current_video = input_video

    for task in plan:

        print("Running task:", task)

        if task == "generate_subtitles":

            current_video = generate_subtitles(current_video)

        elif task == "trim":

            current_video = trim_video(current_video)

        elif task == "remove_silence":

            current_video = remove_silence(current_video)

        elif task == "extract_audio":

            current_video = extract_audio(current_video)

    return current_video
