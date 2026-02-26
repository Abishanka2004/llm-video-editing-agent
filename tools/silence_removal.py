import sys
import os

# FIX PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from moviepy.editor import VideoFileClip
from pydub import AudioSegment, silence
import imageio_ffmpeg
from config import FINAL_OUTPUT

# Fix ffmpeg path
AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()


def remove_silence(input_video):

    video = VideoFileClip(input_video)

    video.audio.write_audiofile("temp.wav")

    sound = AudioSegment.from_wav("temp.wav")

    chunks = silence.split_on_silence(
        sound,
        min_silence_len=700,
        silence_thresh=-40
    )

    combined = sum(chunks)

    combined.export(FINAL_OUTPUT, format="wav")

    return FINAL_OUTPUT
