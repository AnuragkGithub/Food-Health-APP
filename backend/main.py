from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# YOUR GOOGLE API KEY
API_KEY = ""

class FoodRequest(BaseModel):
    food: str
    goal: str

@app.post("/analyze")
def analyze_food(data: FoodRequest):

    prompt = f"""
    Analyze this meal: {data.food}

    User Goal: {data.goal}

    Give:
    1. Health score
    2. Estimated calories
    3. Nutritional analysis
    4. Healthy alternatives
    5. Personalized suggestions
    """

    try:

        # GOOGLE GEMINI API URL
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key={API_KEY}"

        # REQUEST PAYLOAD
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        # SEND REQUEST
        response = requests.post(url, json=payload)

        # CONVERT RESPONSE TO JSON
        result = response.json()

        print(result)

        # CHECK SUCCESS
        if "candidates" in result:

            text = result["candidates"][0]["content"]["parts"][0]["text"]

        else:

            text = f"API Error: {result}"

        return {
            "result": text
        }

    except Exception as e:

        return {
            "result": str(e)
        }