import whisper

model = whisper.load_model("tiny", device="cpu")

def transcribe(video_path):

    result = model.transcribe(video_path)

    return result["text"]
