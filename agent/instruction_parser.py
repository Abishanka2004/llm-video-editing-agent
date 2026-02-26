def parse_instruction(text):

    text = text.lower()

    tasks = []

    # SUBTITLES
    subtitle_keywords = [
        "subtitle",
        "subtitles",
        "caption",
        "captions",
        "transcript"
    ]

    # AUDIO EXTRACTION (removed generic "audio")
    audio_keywords = [
        "extract audio",
        "get audio",
        "convert to audio",
        "audio only",
        "extract mp3",
        "save audio"
    ]

    # TRIM
    trim_keywords = [
        "trim",
        "cut",
        "shorten",
        "clip"
    ]

    # SILENCE REMOVAL
    silence_keywords = [
        "remove silence",
        "remove pauses",
        "remove pause"
    ]


    # CHECK EACH CATEGORY

    if any(keyword in text for keyword in subtitle_keywords):

        tasks.append("generate_subtitles")


    if any(keyword in text for keyword in audio_keywords):

        tasks.append("extract_audio")


    if any(keyword in text for keyword in trim_keywords):

        tasks.append("trim")


    if any(keyword in text for keyword in silence_keywords):

        tasks.append("remove_silence")


    return tasks
