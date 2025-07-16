import streamlit as st
import json

# Load quiz data from JSON
with open("wunderlich_quiz_data.json", "r") as f:
    questions = json.load(f)

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.answers = []

st.title("📝 Pre-employment Assessment")

if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    st.subheader(f"Question {q['id']}")
    selected = st.radio(q["question"], q["options"], key=st.session_state.q_index)

    if st.button("Submit Answer"):
        st.session_state.answers.append({
            "question": q["question"],
            "selected": selected
        })
        st.session_state.q_index += 1
        st.experimental_rerun()
else:
    st.success("🎉 Assessment Completed!")
    st.write(f"You answered {len(st.session_state.answers)} questions.")
    for i, ans in enumerate(st.session_state.answers):
        st.markdown(f"**Q{i+1}:** {ans['question']}")
        st.markdown(f"Your answer: `{ans['selected']}`")
        st.write("---")

    if st.button("Restart Assessment"):
        st.session_state.q_index = 0
        st.session_state.answers = []
        st.experimental_rerun()
