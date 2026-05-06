import streamlit as st
import requests

st.set_page_config(page_title="NutriMind AI")

st.title("🥗 NutriMind AI")
st.subheader("AI Nutrition Intelligence Assistant")

food = st.text_area("What did you eat?")

goal = st.selectbox(
    "Select Your Goal",
    ["Weight Loss", "Muscle Gain", "Healthy Lifestyle"]
)

if st.button("Analyze Meal"):

    payload = {
        "food": food,
        "goal": goal
    }

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json=payload
    )

    if response.status_code == 200:

        result = response.json()

        st.success("Analysis Complete")

        st.markdown(result["result"])

    else:
        st.error(f"Backend error: {response.text}")