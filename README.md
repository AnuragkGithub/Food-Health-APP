
# NutriMind AI

AI-powered Food & Health Assistant using Google Gemini API.

## Features
- AI Meal Analysis
- Personalized Recommendations
- Health Insights
- Dynamic AI Responses
- FastAPI Backend
- Streamlit Frontend

## Tech Stack
- FastAPI
- Streamlit
- Google Gemini API
- Python

## Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add Gemini API key
Create .env file:

GEMINI_API_KEY=your_api_key_here

### 3. Run backend
uvicorn main:app --reload

### 4. Run frontend
streamlit run app.py

## Gemini API
Get your API key from:
https://aistudio.google.com/app/apikey
