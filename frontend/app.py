import streamlit as st
import requests

# ================= PAGE CONFIG ================= #
st.set_page_config(
    page_title="NutriMind AI",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= CUSTOM CSS ================= #
st.markdown("""
<style>

/* GLOBAL */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    scroll-behavior: smooth;
}

.stApp {
    background: linear-gradient(135deg, #081120, #0f172a);
    color: white;
}

/* HIDE STREAMLIT */
header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

/* HERO SECTION */
.hero {
    background: linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.65)
    ),
    url('https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=2070&auto=format&fit=crop');
    
    background-size: cover;
    background-position: center;
    padding: 120px 80px;
    border-radius: 30px;
    margin-top: 20px;
    margin-bottom: 40px;
    box-shadow: 0px 8px 40px rgba(0,0,0,0.4);
}

.hero-title {
    font-size: 72px;
    font-weight: 800;
    line-height: 1.1;
    color: white;
}

.hero-subtitle {
    font-size: 22px;
    color: #E2E8F0;
    margin-top: 20px;
    max-width: 700px;
}

.hero-button {
    margin-top: 30px;
    background: linear-gradient(90deg, #00E5A8, #00BFFF);
    padding: 14px 28px;
    border-radius: 15px;
    color: white;
    display: inline-block;
    font-weight: bold;
    font-size: 18px;
}

/* SECTION TITLES */
.section-title {
    font-size: 42px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
    color: white;
}

/* FEATURE CARDS */
.feature-card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    transition: 0.3s ease;
    height: 240px;
}

.feature-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 30px rgba(0,229,168,0.2);
}

.feature-icon {
    font-size: 60px;
    margin-bottom: 10px;
}

.feature-title {
    font-size: 28px;
    font-weight: bold;
    color: white;
}

.feature-desc {
    color: #CBD5E1;
    margin-top: 15px;
    font-size: 16px;
}

/* ANALYZER CARD */
.analyzer-card {
    background: rgba(255,255,255,0.06);
    border-radius: 30px;
    padding: 40px;
    margin-top: 40px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

/* TEXT AREA */
.stTextArea textarea {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    padding: 18px !important;
    font-size: 17px !important;
}

/* SELECT BOX */
.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.08) !important;
    border-radius: 14px !important;
    color: white !important;
}

/* BUTTON */
.stButton button {
    width: 100%;
    height: 60px;
    border-radius: 18px;
    border: none;
    background: linear-gradient(90deg, #00E5A8, #00BFFF);
    color: white;
    font-size: 20px;
    font-weight: bold;
    transition: 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(0,229,168,0.35);
}

/* RESULT BOX */
.result-box {
    background: rgba(255,255,255,0.06);
    border-radius: 30px;
    padding: 40px;
    margin-top: 40px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* FOOD GALLERY */
.food-card img {
    border-radius: 20px;
    transition: 0.3s ease;
}

.food-card img:hover {
    transform: scale(1.04);
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 50px 0;
    color: #94A3B8;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ================= HERO SECTION ================= #
st.markdown("""
<div class="hero">
    <div class="overlay">
        <h1 class="hero-title">🥗 NutriMind AI</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= FEATURES ================= #
st.markdown(
    '<div class="section-title">✨ Powerful AI Features</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Smart Calories</div>
        <div class="feature-desc">
            AI-powered calorie estimation and detailed nutritional breakdown.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🥗</div>
        <div class="feature-title">Diet Optimization</div>
        <div class="feature-desc">
            Personalized meal suggestions based on your fitness goals.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Health Coach</div>
        <div class="feature-desc">
            Advanced AI recommendations for healthier daily habits.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOD GALLERY ================= #
st.markdown(
    '<div class="section-title">🥑 Healthy Food Inspiration</div>',
    unsafe_allow_html=True
)

g1, g2, g3, g4 = st.columns(4)

with g1:
    st.image(
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800",
        use_container_width=True
    )

with g2:
    st.image(
        "https://images.unsplash.com/photo-1498837167922-ddd27525d352?q=80&w=800",
        use_container_width=True
    )

with g3:
    st.image(
        "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?q=80&w=800",
        use_container_width=True
    )

with g4:
    st.image(
        "https://images.unsplash.com/photo-1502741338009-cac2772e18bc?q=80&w=800",
        use_container_width=True
    )

# ================= ANALYZER ================= #
st.markdown(
    '<div class="section-title">🧠 AI Meal Analyzer</div>',
    unsafe_allow_html=True
)

food = st.text_area(
    "🍽️ What did you eat today?",
    placeholder="Example: Burger, biryani, fries, cold coffee..."
)

goal = st.selectbox(
    "🎯 Select Your Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "Healthy Lifestyle"
    ]
)

analyze = st.button("🚀 Analyze My Meal")

st.markdown('</div>', unsafe_allow_html=True)

# ================= ANALYSIS ================= #
if analyze:

    if not food.strip():

        st.warning("Please enter your meal details.")

    else:

        payload = {
            "food": food,
            "goal": goal
        }

        try:

            with st.spinner("🧠 NutriMind AI is analyzing your meal..."):

                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json=payload
                )

            if response.status_code == 200:

                result = response.json()

                st.markdown("""
                <div class="result-box">
                    <h1>✅ Nutrition Analysis Complete</h1>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(result["result"])

            else:
                st.error(f"Backend Error: {response.text}")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ================= FOOTER ================= #
st.markdown("""
<div class="footer">
    🚀 Powered by Groq + Llama 3 + Streamlit <br>
    Built with ❤️ for AI Health Innovation
</div>
""", unsafe_allow_html=True)