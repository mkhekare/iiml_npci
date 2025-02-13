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

# Streamlit App Header
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            max-width: 1100px;
            margin: auto;
            padding: 2rem;
            border-radius: 12px;
            background: linear-gradient(145deg, #2C2C2C, #3D3D3D);
        }
        .content-box {
            background-color: #1E1E1E;
            padding: 1.5rem;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💎 RuPay Luxe Rewards Program")
st.subheader("Experience luxury, exclusivity, and unparalleled rewards.")

# Layouting Sections
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.sidebar.title("User Profile")
    st.sidebar.subheader("Tell us about yourself")
    existing_user = st.sidebar.radio("Are you an existing RuPay Cardholder?", ["Yes", "No"])
    cibil_score = st.sidebar.slider("Your CIBIL Score", min_value=300, max_value=900, step=10)
    card_experience = st.sidebar.selectbox("Your experience with credit cards", ["Beginner", "Intermediate", "Expert"])

with col2:
    st.subheader("💰 Eligibility & Calculation")
    annual_spending = st.number_input("Enter your annual spending (in ₹):", min_value=0, step=50000)
    
    def filter_cards(annual_spending, cibil_score):
        eligible_cards = df[df["Eligibility"].apply(lambda x: x if isinstance(x, int) else float('inf')) <= annual_spending]
        if cibil_score < 650:
            eligible_cards = eligible_cards[eligible_cards["Tier"].isin(["Luxe Silver", "Luxe Gold"])]
        return eligible_cards

    eligible_cards = filter_cards(annual_spending, cibil_score)

    if not eligible_cards.empty:
        st.success("✅ Based on your profile, you are eligible for the following card(s):")
        st.table(eligible_cards.drop(columns=["Eligibility"]))
    else:
        st.warning("⚠️ No cards available for your spending level or credit profile.")

with col3:
    st.subheader("📌 Luxe Rewards Details")
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

# Footer
st.caption("Designed for the elite. Elevate your lifestyle with RuPay Luxe Rewards.")
