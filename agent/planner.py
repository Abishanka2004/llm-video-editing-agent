def create_plan(tasks):

    plan = []

    for task in tasks:

        if task == "generate_subtitles":

            plan.append("generate_subtitles")

        elif task == "trim":

            plan.append("trim")

        elif task == "remove_silence":

            plan.append("remove_silence")

        elif task == "extract_audio":

            plan.append("extract_audio")

    return plan
