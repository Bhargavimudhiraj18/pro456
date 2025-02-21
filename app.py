import streamlit as st
import google.generativeai as genai

# Set up Google Gemini API Key
GEMINI_API_KEY = "AIzaSyAmbAt2a6mCtgXPbO2hTKiK9x8IMa1ojWY"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate AI-powered study plan
def generate_study_plan(subjects, available_hours):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Create a detailed study plan for a student with {available_hours} study hours per day.
    Subjects and deadlines:
    {subjects}

    The plan should:
    - Allocate daily study hours proportionally based on deadlines.
    - Adjust dynamically if a session is missed.
    - Include a Pomodoro cycle (25 min study, 5 min break).
    - Suggest optimal break times.

    Return output in an easy-to-read format.
    """

    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("📚 AI-Powered Study Planner")

# User Inputs
st.sidebar.header("Enter Study Details")
subjects = {}
num_subjects = st.sidebar.number_input("How many subjects?", 1, 10, 3, key="num_subjects")

for i in range(num_subjects):
    subject = st.sidebar.text_input(f"Subject {i+1} Name", key=f"subject_{i}")
    hours = st.sidebar.number_input(f"Total Hours for {subject}", 1, 100, 10, key=f"hours_{i}")
    deadline = st.sidebar.date_input(f"Deadline for {subject}", key=f"deadline_{i}")

    if subject:
        subjects[subject] = {"hours": hours, "deadline": deadline.strftime("%Y-%m-%d")}

available_hours = st.sidebar.slider("Daily Study Hours", 1, 12, 4, key="available_hours")

# Generate Study Plan
if st.sidebar.button("Generate Study Plan", key="generate_button"):
    if subjects:
        study_plan = generate_study_plan(subjects, available_hours)
        st.subheader("📅 Your AI-Generated Study Plan")
        st.write(study_plan)
    else:
        st.warning("Please enter at least one subject!")



