import streamlit as st
import pandas as pd

# Define card tiers data
tiers = [
    {"Tier": "Luxe Silver", "Eligibility": 500000, "Points": 1.5, "Lounge Access": "4 domestic visits/year", "Benefits": "Birthday month bonus: 2x points on all spends"},
    {"Tier": "Luxe Gold", "Eligibility": 1000000, "Points": 2, "Lounge Access": "6 international visits/year", "Benefits": "Priority customer service with a dedicated relationship manager"},
    {"Tier": "Luxe Platinum", "Eligibility": 2000000, "Points": 3, "Lounge Access": "Unlimited global", "Benefits": "Personalized concierge, luxury brand invites"},
    {"Tier": "Luxe Black", "Eligibility": "Invitation only", "Points": 4, "Lounge Access": "Unlimited global with VIP services", "Benefits": "Exclusive events, luxury travel packages"},
    {"Tier": "Luxe Ultra", "Eligibility": "Invitation only", "Points": 5, "Lounge Access": "Unlimited global with VIP services", "Benefits": "Dedicated lifestyle manager, ultra-exclusive events"}
]

df = pd.DataFrame(tiers)

# Streamlit App Styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            max-width: 1300px;
            margin: auto;
            padding: 2rem;
            border-radius: 12px;
            background: linear-gradient(145deg, #1C1C1C, #2D2D2D);
        }
        .content-box {
            background-color: #333333;
            padding: 1.8rem;
            border-radius: 12px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
            color: #ffffff;
            margin-bottom: 25px;
        }
        .sidebar .css-1aumxhk, .sidebar .css-18e3th9 {
            color: #ffffff !important;
        }
        h1 {
            font-size: 36px;
            color: #FFD700;
        }
        h2 {
            font-size: 28px;
            color: #FFA500;
        }
        h3 {
            font-size: 24px;
            color: #FF8C00;
        }
        p, li {
            font-size: 18px;
            line-height: 1.8;
            color: #CCCCCC;
        }
        .success-box {
            background-color: #004d00;
            padding: 12px;
            border-radius: 6px;
            color: white;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💎 RuPay Luxe Rewards Program")
st.subheader("Experience luxury, exclusivity, and unparalleled rewards.")

# Layouting Sections
st.markdown("### 🧑‍💼 User Profile")
st.markdown("<div class='content-box'>", unsafe_allow_html=True)
st.sidebar.title("User Profile")
st.sidebar.subheader("Tell us about yourself")
existing_user = st.sidebar.radio("Are you an existing RuPay Cardholder?", ["Yes", "No"])
cibil_score = st.sidebar.slider("Your CIBIL Score", min_value=300, max_value=900, step=10)
card_experience = st.sidebar.selectbox("Your experience with credit cards", ["Beginner", "Intermediate", "Expert"])
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("### 💰 Eligibility & Calculation")
st.markdown("<div class='content-box'>", unsafe_allow_html=True)
annual_spending = st.number_input("Enter your annual spending (in ₹):", min_value=0, step=50000)

def filter_cards(annual_spending, cibil_score):
    eligible_cards = df[df["Eligibility"].apply(lambda x: x if isinstance(x, int) else float('inf')) <= annual_spending]
    if cibil_score < 650:
        eligible_cards = eligible_cards[eligible_cards["Tier"].isin(["Luxe Silver", "Luxe Gold"])]
    return eligible_cards

eligible_cards = filter_cards(annual_spending, cibil_score)

if not eligible_cards.empty:
    st.markdown("<div class='success-box'>✅ Based on your profile, you are eligible for the following card(s):</div>", unsafe_allow_html=True)
    st.table(eligible_cards.drop(columns=["Eligibility"]))
else:
    st.warning("⚠️ No cards available for your spending level or credit profile.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("### 📌 Luxe Rewards Details")
st.markdown("<div class='content-box'>", unsafe_allow_html=True)
st.write("RuPay Luxe Rewards is designed to attract and retain affluent customers by offering unparalleled benefits and experiences.")
st.write("- **Personalized Rewards**: Tailored to individual spending habits and preferences.")
st.write("- **Exclusive Access**: VIP events, luxury travel perks, and bespoke services.")
st.write("- **High Reward Rates**: Accelerated points on premium spending categories.")
st.write("- **Global Benefits**: Internationally recognized rewards and benefits.")

st.subheader("🚀 Accelerated Rewards")
st.write("- **Luxury Retail**: 5x points at partner luxury brands 🛍️")
st.write("- **Fine Dining**: 3x points at gourmet restaurants 🍽️")
st.write("- **Travel**: 4x points on flight and hotel bookings ✈️🏨")

st.subheader("🎁 Redemption Options")
st.write("- **Exclusive Merchandise**: Redeem points for luxury products and services 🎁")
st.write("- **Travel Benefits**: Use points for flight upgrades, hotel stays, and vacation packages 🏝️")
st.write("- **Experiential Rewards**: Private concerts, art exhibitions, and gourmet cooking classes 🎨🎶")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.caption("Designed for the elite. Elevate your lifestyle with RuPay Luxe Rewards.")
