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
            background-color: #F5F5F5; /* Light background for a fresh look */
            color: #333333; /* Dark text for better readability */
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            max-width: 1100px;
            margin: auto;
            padding: 2rem;
            border-radius: 12px;
            background: linear-gradient(145deg, #EAEAEA, #D1D1D1); /* Softer gradient */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
        }
        .content-box {
            background-color: #FFFFFF; /* White background for content boxes */
            padding: 1.5rem;
            border-radius: 12px;
            color: #333333; /* Dark text for content */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Light shadow for content boxes */
        }
        .sidebar .css-1aumxhk, .sidebar .css-18e3th9 {
            color: #333333 !important; /* Darker text in the sidebar */
        }
        h1, h2, h3 {
            color: #444444; /* Slightly darker headers */
        }
        p {
            line-height: 1.6; /* Improved readability */
        }
    </style>
""", unsafe_allow_html=True)


st.title("💎 RuPay Luxe Rewards Program")
st.subheader("Experience luxury, exclusivity, and unparalleled rewards.")

# Layouting Sections
st.markdown("### User Profile")
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
    st.success("✅ Based on your profile, you are eligible for the following card(s):")
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
