import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("."))

import streamlit as st

from agent.instruction_parser import parse_instruction
from agent.planner import create_plan
from agent.llm_langgraph_agent import create_agent


st.title("🎬 Video Editor Agent")

video_file = st.file_uploader("Upload Video", type=["mp4"])

instruction = st.text_input("Enter Editing Instruction")

if st.button("Run Agent"):

    if video_file is not None:

        os.makedirs("output", exist_ok=True)

        with open("output/input.mp4", "wb") as f:
            f.write(video_file.read())

        st.write("Parsing instruction...")
        tasks = parse_instruction(instruction)

        # ✅ DEBUG LINE ADDED HERE
        st.write("Tasks identified:", tasks)

        st.write("Planning...")
        plan = create_plan(tasks)

        st.write("Executing agent...")
        #final_video = execute(plan, "output/input.mp4")

        agent = create_agent()

        result = agent.invoke({

            "input_video": "output/input.mp4",
            "instruction": instruction

            })

        final_video = result["output"]


        st.success("Done!")

        if final_video.endswith(".mp4"):
            st.video(final_video)

        elif final_video.endswith(".mp3"):
            st.audio(final_video)
