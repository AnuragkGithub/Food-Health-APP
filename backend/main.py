from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()

# ---------------- CORS ---------------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- GROQ CLIENT ---------------- #
client = OpenAI(
    api_key="",
    base_url="https://api.groq.com/openai/v1"
)

# ---------------- REQUEST MODEL ---------------- #
class FoodRequest(BaseModel):
    food: str
    goal: str

# ---------------- API ROUTE ---------------- #
@app.post("/analyze")
def analyze_food(data: FoodRequest):

    prompt = f"""
    Analyze this meal: {data.food}

    User Goal: {data.goal}

    Give response in beautiful markdown format.

    Include:
    1. Health Score (/10)
    2. Estimated Calories
    3. Protein / Carbs / Fat breakdown
    4. Nutritional Analysis
    5. Healthy Alternatives
    6. Personalized Suggestions
    7. Best foods to eat next
    """

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": """
                    You are NutriMind AI,
                    an advanced AI Nutrition Intelligence Assistant.

                    Give smart, modern, professional,
                    health-focused nutrition advice.
                    """
                },

                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,
            max_tokens=1200
        )

        text = response.choices[0].message.content

        return {
            "result": text
        }

    except Exception as e:

        return {
            "result": f"API Error: {str(e)}"
        }