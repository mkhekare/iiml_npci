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
# Streamlit App Header
st.markdown("""
    <style>
        body {
            background-color: #0A0A0A; /* Darker background for elegance */
            color: #EAEAEA; /* Soft light color for contrast */
            font-family: 'Georgia', serif; /* Elegant font choice */
        }
        .stApp {
            max-width: 1200px; /* Slightly wider for spacious feel */
            margin: auto;
            padding: 3rem; /* Increased padding for luxury feel */
            border-radius: 20px; /* More rounded corners */
            background: linear-gradient(145deg, #2C2C2C, #4B4B4B); /* Softer gradient */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5); /* Shadow for depth */
        }
        .sidebar {
            background-color: #1C1C1C; /* Slightly lighter sidebar */
            padding: 2rem; /* More padding for a luxurious look */
            border-radius: 20px; /* Rounded corners */
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); /* Shadow for depth */
        }
        h1, h2, h3 {
            font-family: 'Times New Roman', serif; /* Elegant header font */
            font-weight: bold; /* Bold headers for emphasis */
        }
        p {
            line-height: 1.6; /* Improved readability */
        }
    </style>
""", unsafe_allow_html=True)


st.title("💎 RuPay Luxe Rewards Program")
st.subheader("Experience luxury, exclusivity, and unparalleled rewards.")

# Sidebar for additional inputs
st.sidebar.title("User Profile")
st.sidebar.subheader("Tell us about yourself")
existing_user = st.sidebar.radio("Are you an existing RuPay Cardholder?", ["Yes", "No"])
cibil_score = st.sidebar.slider("Your CIBIL Score", min_value=300, max_value=900, step=10)
card_experience = st.sidebar.selectbox("Your experience with credit cards", ["Beginner", "Intermediate", "Expert"])

# User Input
annual_spending = st.number_input("Enter your annual spending (in ₹):", min_value=0, step=50000)

# Filter cards based on spending and CIBIL score
def filter_cards(annual_spending, cibil_score):
    eligible_cards = df[df["Eligibility"].apply(lambda x: x if isinstance(x, int) else float('inf')) <= annual_spending]
    if cibil_score < 650:
        eligible_cards = eligible_cards[eligible_cards["Tier"].isin(["Luxe Silver", "Luxe Gold"])]
    return eligible_cards

eligible_cards = filter_cards(annual_spending, cibil_score)

# Display results
if not eligible_cards.empty:
    st.success("✅ Based on your profile, you are eligible for the following card(s):")
    st.table(eligible_cards.drop(columns=["Eligibility"]))
else:
    st.warning("⚠️ No cards available for your spending level or credit profile.")

# Layout with Rewards Model on one side
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("🚀 Accelerated Rewards on Premium Categories")
    st.write("- **Luxury Retail**: 5x points at partner luxury brands 🛍️")
    st.write("- **Fine Dining**: 3x points at gourmet restaurants 🍽️")
    st.write("- **Travel**: 4x points on flight and hotel bookings ✈️🏨")

    st.subheader("🎁 Redemption Options")
    st.write("- **Exclusive Merchandise**: Redeem points for luxury products and services 🎁")
    st.write("- **Travel Benefits**: Use points for flight upgrades, hotel stays, and vacation packages 🏝️")
    st.write("- **Experiential Rewards**: Private concerts, art exhibitions, and gourmet cooking classes 🎨🎶")

with col2:
    st.subheader("🔹 Loyalty & Rewards Model")
    st.write("RuPay Luxe Rewards is designed to attract and retain affluent customers by offering unparalleled benefits and experiences.")
    
    st.subheader("📌 Key Features of RuPay Luxe Rewards")
    st.write("- **Personalized Rewards**: Tailored to individual spending habits and preferences.")
    st.write("- **Exclusive Access**: VIP events, luxury travel perks, and bespoke services.")
    st.write("- **High Reward Rates**: Accelerated points on premium spending categories.")
    st.write("- **Global Benefits**: Internationally recognized rewards and benefits.")

st.subheader("🤝 Strategic Partnerships")
st.write("- **Luxury Brand Collaborations**: Partnering with high-end brands for exclusive access and benefits.")
st.write("- **Travel & Hospitality Alliances**: Premium airline and luxury hotel benefits.")
st.write("- **Fine Dining Partnerships**: Michelin-starred dining experiences.")

st.subheader("📡 AI-Driven Personalized Engagement")
st.write("- **Behavioral Analysis**: AI-driven insights for customized offers.")
st.write("- **Exclusive Digital Platform**: 24/7 concierge services and real-time notifications.")

st.subheader("📊 Monitoring & Feedback Mechanism")
st.write("- **Customer Surveys**: Regular insights on satisfaction and improvements.")
st.write("- **Performance Metrics**: Tracking engagement and retention KPIs.")

# Footer
st.caption("Designed for the elite. Elevate your lifestyle with RuPay Luxe Rewards.")
