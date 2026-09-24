# ----------------- ATTRACTIVE MECHANICAL WALLPAPER & STYLING ----------------- #
st.markdown("""
<style>
    /* Mechanical Engineering Blueprint & Carbon Dark Wallpaper */
    .stApp {
        background-image: 
            linear-gradient(rgba(11, 15, 25, 0.88), rgba(11, 15, 25, 0.92)),
            url("https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
        font-family: 'Segoe UI', -apple-system, Roboto, sans-serif;
    }

    /* Glassmorphism Profile Badge */
    .student-badge {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 2px solid #f59e0b;
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
    }
    .badge-name {
        font-size: 1.4rem;
        font-weight: 800;
        color: #fbbf24;
        letter-spacing: 0.8px;
    }
    .badge-sub {
        font-size: 0.95rem;
        color: #cbd5e1;
        margin-top: 4px;
    }

    /* Glassmorphism Card Panels for Inputs & Tools */
    div[data-testid="stVerticalBlock"] > div:has(div.stNumberInput, div.stSelectbox) {
        background: rgba(15, 23, 42, 0.75);
        padding: 18px;
        border-radius: 14px;
        border: 1px solid rgba(245, 158, 11, 0.25);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(6px);
        margin-bottom: 12px;
    }

    /* 3D Tactile Ember Gold Buttons */
    div.stButton > button {
        background: linear-gradient(180deg, #f59e0b 0%, #d97706 50%, #b45309 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: 1px solid #78350f !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 0 #78350f, 0 8px 15px rgba(0, 0, 0, 0.45) !important;
        cursor: pointer !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(180deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%) !important;
        color: #ffffff !important;
    }
    div.stButton > button:active {
        box-shadow: 0 1px 0 #78350f !important;
    }

    /* Simulation Output Box */
    .demo-card {
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(245, 158, 11, 0.4);
        border-radius: 12px;
        padding: 16px;
        margin: 14px 0px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
    }
</style>
""", unsafe_allow_html=True)
