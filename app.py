import streamlit as st
import pandas as pd
from datetime import datetime

# Define card tiers data
tiers = [
    {
        "Tier": "Luxe Silver",
        "Eligibility": 500000,
        "Points": 1.5,
        "Lounge Access": "4 domestic visits/year",
        "Benefits": "Birthday month bonus: 2x points on all spends",
    },
    {
        "Tier": "Luxe Gold",
        "Eligibility": 1000000,
        "Points": 2,
        "Lounge Access": "6 international visits/year",
        "Benefits": "Priority customer service with dedicated RM",
    },
    {
        "Tier": "Luxe Platinum",
        "Eligibility": 2000000,
        "Points": 3,
        "Lounge Access": "Unlimited global",
        "Benefits": "Personalized concierge, luxury brand invites",
    },
    {
        "Tier": "Luxe Black",
        "Eligibility": "Invitation only",
        "Points": 4,
        "Lounge Access": "Unlimited global with VIP",
        "Benefits": "Exclusive events, luxury travel packages",
    }
]

df = pd.DataFrame(tiers)

# Streamlit configuration
st.set_page_config(layout="wide", page_title="RuPay Luxe Rewards", page_icon="💎")

# Simplified styling
st.markdown("""
    <style>
        .main-container {
            padding: 0rem 1rem;
        }
        .stApp {
            background-color: white;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
        .title {
            color: #1a237e;
            text-align: center;
            font-size: 24px;
            padding: 10px 0;
            margin-bottom: 20px;
            border-bottom: 2px solid #1a237e;
        }
        .section-box {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            background-color: white;
            height: 100%;
        }
        .section-title {
            color: #1a237e;
            font-size: 18px;
            margin-bottom: 10px;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }
        .benefit-list {
            list-style-type: none;
            padding-left: 0;
            margin: 5px 0;
        }
        .benefit-item {
            margin: 5px 0;
            font-size: 14px;
        }
        .card-tier {
            border: 1px solid #eee;
            border-radius: 5px;
            padding: 8px;
            margin: 5px 0;
            background-color: #f8f9fa;
        }
        .footer {
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 10px;
            border-top: 1px solid #eee;
        }
        div[data-testid="stVerticalBlock"] > div {
            padding-top: 0;
        }
        div[class*="stMarkdown"] p {
            font-size: 14px;
            margin: 0;
            padding: 2px 0;
        }
        .stRadio > label {
            font-size: 14px;
        }
        .stSelectbox > label {
            font-size: 14px;
        }
        .stNumberInput > label {
            font-size: 14px;
        }
        .stSlider > label {
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">💎 RuPay Luxe Rewards Program</h1>', unsafe_allow_html=True)

# Create three columns for layout
col1, col2, col3 = st.columns([1, 1.2, 1])

# Column 1: User Profile
with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧑‍💼 User Profile</div>', unsafe_allow_html=True)
    
    existing_user = st.radio("Existing RuPay Cardholder?", ["Yes", "No"], horizontal=True)
    cibil_score = st.slider("CIBIL Score", 300, 900, 750, 50)
    card_experience = st.selectbox("Card Experience", ["Beginner", "Intermediate", "Expert"])
    occupation = st.selectbox("Occupation", ["Salaried", "Self-employed", "Business Owner"])
    annual_income = st.number_input("Annual Income (₹)", 0, 10000000, 500000, 100000)
    st.markdown('</div>', unsafe_allow_html=True)

# Column 2: Eligibility Calculator
with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💰 Eligibility Calculator</div>', unsafe_allow_html=True)
    
    annual_spending = st.number_input("Annual Spending (₹)", 0, 5000000, 100000, 50000)

    def calculate_eligibility(spending, score, income):
        eligible_cards = []
        for tier in tiers:
            eligibility = tier["Eligibility"]
            if isinstance(eligibility, str):
                continue
            if spending >= eligibility and score >= 650 and income >= eligibility * 0.3:
                eligible_cards.append(tier)
        return eligible_cards

    eligible_cards = calculate_eligibility(annual_spending, cibil_score, annual_income)

    if eligible_cards:
        for card in eligible_cards:
            st.markdown(f"""
                <div class="card-tier">
                    <b>{card["Tier"]}</b><br>
                    Points: {card["Points"]}x • {card["Lounge Access"]}<br>
                    {card["Benefits"]}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No cards available for current profile")
    st.markdown('</div>', unsafe_allow_html=True)

# Column 3: Program Details
with col3:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📌 Program Details</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <b>🎯 Core Benefits</b>
        <ul class="benefit-list">
            <li class="benefit-item">• Personalized Rewards</li>
            <li class="benefit-item">• Exclusive Access</li>
            <li class="benefit-item">• High Reward Rates</li>
        </ul>
        
        <b>🚀 Accelerated Rewards</b>
        <ul class="benefit-list">
            <li class="benefit-item">• 5x points - Luxury Retail</li>
            <li class="benefit-item">• 3x points - Fine Dining</li>
            <li class="benefit-item">• 4x points - Travel</li>
        </ul>
        
        <b>🎁 Redemption Options</b>
        <ul class="benefit-list">
            <li class="benefit-item">• Luxury Merchandise</li>
            <li class="benefit-item">• Travel Benefits</li>
            <li class="benefit-item">• Experiential Rewards</li>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
    <div class="footer">
        Designed for the elite. Elevate your lifestyle with RuPay Luxe Rewards.<br>
        © {datetime.now().year} RuPay Luxe. All rights reserved.
    </div>
""", unsafe_allow_html=True)
