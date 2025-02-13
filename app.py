import streamlit as st
import pandas as pd
from datetime import datetime

# Define card tiers data with enhanced benefits
tiers = [
    {
        "Tier": "Luxe Silver",
        "Eligibility": 500000,
        "Points": 1.5,
        "Lounge Access": "4 domestic visits/year",
        "Benefits": "2x birthday points, free movie tickets",
        "Color": "#C0C0C0"
    },
    {
        "Tier": "Luxe Gold",
        "Eligibility": 1000000,
        "Points": 2,
        "Lounge Access": "6 international visits/year",
        "Benefits": "Dedicated RM, golf access",
        "Color": "#FFD700"
    },
    {
        "Tier": "Luxe Platinum",
        "Eligibility": 2000000,
        "Points": 3,
        "Lounge Access": "Unlimited global",
        "Benefits": "Concierge, luxury brand access",
        "Color": "#E5E4E2"
    },
    {
        "Tier": "Luxe Black",
        "Eligibility": "Invitation only",
        "Points": 4,
        "Lounge Access": "Unlimited VIP global",
        "Benefits": "Private events, luxury travel",
        "Color": "#000000"
    }
]

df = pd.DataFrame(tiers)

# Streamlit configuration
st.set_page_config(layout="wide", page_title="RuPay Luxe Rewards", page_icon="💎", initial_sidebar_state="collapsed")

# Enhanced styling with reduced top spacing
st.markdown("""
    <style>
        /* Remove top padding and header spacing */
        .stApp {
            background-color: white;
            margin-top: -80px;
        }
        .main-container {
            padding: 0 1rem;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
        /* Header styling */
        .title-container {
            background-color: white;
            padding: 15px 0 5px 0;
            margin-bottom: 15px;
            border-bottom: 2px solid #1a237e;
        }
        .title {
            color: #1a237e;
            text-align: center;
            font-size: 26px;
            font-weight: 600;
            margin: 0;
        }
        /* Section styling */
        .section-box {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            background-color: white;
            height: 100%;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .section-title {
            color: #1a237e;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 2px solid #f0f0f0;
        }
        /* Card tier styling */
        .card-tier {
            border: 1px solid #eee;
            border-radius: 8px;
            padding: 12px;
            margin: 8px 0;
            background: linear-gradient(to right, #fff, #fafafa);
            transition: transform 0.2s;
        }
        .card-tier:hover {
            transform: translateX(5px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .card-name {
            font-weight: 600;
            color: #1a237e;
            margin-bottom: 5px;
        }
        /* Form elements styling */
        .stRadio > label {
            font-size: 14px;
            font-weight: 500;
        }
        .stSelectbox > label {
            font-size: 14px;
            font-weight: 500;
        }
        .stNumberInput > label {
            font-size: 14px;
            font-weight: 500;
        }
        .stSlider > label {
            font-size: 14px;
            font-weight: 500;
        }
        
        /* Benefits list styling */
        .benefit-list {
            list-style-type: none;
            padding-left: 0;
            margin: 5px 0;
        }
        .benefit-item {
            margin: 6px 0;
            font-size: 14px;
            display: flex;
            align-items: center;
        }
        .benefit-icon {
            margin-right: 8px;
            color: #1a237e;
        }
        /* Footer styling */
        .footer {
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 10px;
            border-top: 1px solid #eee;
            margin-top: 10px;
        }
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        /* Eligibility indicator */
        .eligibility-status {
            padding: 8px;
            border-radius: 6px;
            margin-bottom: 10px;
            font-size: 14px;
            font-weight: 500;
        }
        .eligible {
            background-color: #e8f5e9;
            color: #2e7d32;
            border: 1px solid #a5d6a7;
        }
        .not-eligible {
            background-color: #fff3e0;
            color: #e65100;
            border: 1px solid #ffcc80;
        }
        /* Remove extra padding from Streamlit elements */
        div[data-testid="stVerticalBlock"] > div {
            padding-top: 0;
        }
        .stRadio > div[role="radiogroup"] {
            padding-top: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Custom CSS to remove space and optimize image display
st.markdown("""
    <style>
        .header-image {
            display: block;
            margin-top: -20px;  /* Adjust to remove space */
            margin-bottom: -30px; /* Reduce space between image and title */
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Display the image with optimized spacing
st.image("head.png", use_container_width=True, output_format="auto")

# Main title (RuPay Luxe Rewards Program)
st.markdown("<h1 class='title'>💎 RuPay Luxe Rewards Program</h1>", unsafe_allow_html=True)

# Create three columns for layout
col1, col2, col3 = st.columns([1, 1.2, 1])


# Column 1: User Profile
with col1:
    st.markdown("""
    <div class="box-container">
        <b>🧑‍💼 User Profile</b>
    </div>
""", unsafe_allow_html=True)
    
    existing_user = st.radio("Existing RuPay Cardholder?", ["Yes", "No"], horizontal=True)
    cibil_score = st.slider("CIBIL Score", 300, 900, 750, 50)
    card_experience = st.selectbox("Card Experience", ["Beginner", "Intermediate", "Expert"])
    occupation = st.selectbox("Occupation", ["Salaried", "Self-employed", "Business Owner"])
    annual_income = st.number_input("Annual Income (₹)", 0, 10000000, 500000, 100000)
    st.markdown('</div>', unsafe_allow_html=True)

# Column 2: Eligibility Calculator
with col2:
    st.markdown("""
    <div class="box-container">
        <b><b>💰 Eligibility Calculator</b></b>
    </div>
""", unsafe_allow_html=True)
    
    annual_spending = st.number_input("Annual Spending (₹)", 0, 5000000, 100000, 50000)

    def calculate_eligibility(spending, score, income):
        eligible_cards = []
        min_income_ratio = 0.3  # Minimum income to spending ratio
        
        for tier in tiers:
            eligibility = tier["Eligibility"]
            if isinstance(eligibility, str):  # Skip invitation-only cards
                continue
                
            # Enhanced eligibility criteria
            meets_spending = spending >= eligibility
            meets_credit = score >= 650
            meets_income = income >= eligibility * min_income_ratio
            
            if meets_spending and meets_credit and meets_income:
                eligible_cards.append(tier)
        
        return eligible_cards

    eligible_cards = calculate_eligibility(annual_spending, cibil_score, annual_income)

    if eligible_cards:
        st.markdown("""
            <div class="eligibility-status eligible">
                ✨ Congratulations! You qualify for the following cards:
            </div>
        """, unsafe_allow_html=True)
        
        for card in eligible_cards:
            st.markdown(f"""
                <div class="card-tier" style="border-left: 4px solid {card['Color']}">
                    <div class="card-name">{card['Tier']}</div>
                    <div style="font-size: 14px;">
                        🎯 {card['Points']}x Points on Purchases<br>
                        ✈️ {card['Lounge Access']}<br>
                        🎁 {card['Benefits']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="eligibility-status not-eligible">
                ℹ️ Currently, no cards match your profile. Consider:
                <ul style="margin: 5px 0; padding-left: 20px;">
                    <li>Higher annual spending</li>
                    <li>Improved CIBIL score</li>
                    <li>Increased annual income</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="box-container">
        <b><b>📌 Program Details</b></b>
    </div>
""", unsafe_allow_html=True)

# Fix styling and structure
    st.markdown("""
    <style>
        .box-container {
            border: 2px solid #ddd;
            padding: 15px;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .benefit-list {
            list-style-type: none;
            padding-left: 0;
        }
        .benefit-item {
            font-size: 18px;
            margin-bottom: 5px;
        }
        .title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>

    <div class="box-container">
        <div class="title">🚀 Accelerated Rewards</div>
        <ul class="benefit-list">
            <li class="benefit-item">🛍️ <b>5x points</b> - Luxury Retail</li>
            <li class="benefit-item">🍽️ <b>3x points</b> - Fine Dining</li>
            <li class="benefit-item">✈️ <b>4x points</b> - Travel</li>
        <div class="title">🎁 Redemption Options</div>
        <ul class="benefit-list">
            <li class="benefit-item">🎀 Luxury Merchandise</li>
            <li class="benefit-item">🌟 Travel Benefits</li>
            <li class="benefit-item">🎪 Experiential Rewards</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


# Footer
st.markdown(f"""
    <div class="footer">
        Designed for the elite. Elevate your lifestyle with RuPay Luxe Rewards.<br>
        © {datetime.now().year} RuPay Luxe. All rights reserved.
    </div>
""", unsafe_allow_html=True)
