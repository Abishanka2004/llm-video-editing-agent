import os
import subprocess

def remove_silence(input_video):

    print("Removing silence from video...")

    output_video = "output/no_silence.mp4"

    command = [
        "ffmpeg",
        "-y",
        "-i", input_video,
        "-af",
        "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.5:stop_periods=-1:stop_threshold=-50dB:stop_silence=0.5",
        "-c:v", "copy",
        output_video
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Silence removal complete")

    return output_video