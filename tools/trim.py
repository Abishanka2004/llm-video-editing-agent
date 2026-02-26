import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from moviepy.editor import VideoFileClip
from config import FINAL_OUTPUT

def trim_video(input_path, start=0, end=10):

    print("Trimming Video....")

    clip = VideoFileClip(input_path)

    trimmed = clip.subclip(start, end)

    trimmed.write_videofile(FINAL_OUTPUT)

    print("Trim Complete")

    return FINAL_OUTPUT
