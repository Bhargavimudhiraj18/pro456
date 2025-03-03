import streamlit as st
import google.generativeai as genai

# Set up Google Gemini API Key
GEMINI_API_KEY = "AIzaSyC7qpsSKysdqqE7tn-FxpW71h83Dkt3UtY"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate AI-powered study plan
def generate_study_plan(subjects, available_hours):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Create a detailed study plan for a student with {available_hours} study hours per day.
    Subjects and deadlines: {subjects}
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
subjects = st.sidebar.text_area("Subjects and Deadlines", "")
available_hours = st.sidebar.slider("Available Study Hours per Day", min_value=1, max_value=24, value=6)

if st.sidebar.button("Generate Plan"):
    if subjects:
        plan = generate_study_plan(subjects, available_hours)
        st.write(plan)
    else:
        st.write("Please enter your subjects and deadlines.")

        



