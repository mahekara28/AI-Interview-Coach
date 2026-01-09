# app.py

import streamlit as st
from evaluator_module import generate_feedback
from questions import QUESTIONS

st.set_page_config(page_title="AI Interview Coach", layout="centered")
st.title("🤖 AI Interview Coach")

# Select topic
topic = st.selectbox("Choose Interview Topic", QUESTIONS.keys())
question_data = QUESTIONS[topic]

# Display question
st.subheader("Interview Question")
st.write(question_data["question"])

# Get user input
answer = st.text_area("Type your answer here", height=200)

# Evaluate answer
if st.button("Evaluate Answer"):
    if len(answer.strip()) < 20:
        st.warning("Please write a more detailed answer (at least 20 characters).")
    else:
        result = generate_feedback(answer, question_data["keywords"])

        st.subheader("📊 Evaluation Results")
        st.write("**Clarity Score:**", result["clarity_score"], "/10")
        st.write("**Relevance Score:**", result["relevance_score"], "/10")
        st.write("**Filler Words Used:**", result["fillers"])
        st.write("**Keywords Covered:**", result["found_keywords"])

        st.subheader("📝 Feedback")
        for f in result["feedback"]:
            st.write("•", f)
