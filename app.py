import streamlit as st
import pandas as pd
from datetime import datetime

# Define card tiers data with enhanced structure
tiers = [
    {
        "Tier": "Luxe Silver",
        "Eligibility": 500000,
        "Points": 1.5,
        "Lounge Access": "4 domestic visits/year",
        "Benefits": [
            "Birthday month bonus: 2x points on all spends",
            "Complimentary movie tickets quarterly",
            "Priority customer service"
        ],
        "Color": "#C0C0C0"
    },
    {
        "Tier": "Luxe Gold",
        "Eligibility": 1000000,
        "Points": 2,
        "Lounge Access": "6 international visits/year",
        "Benefits": [
            "Priority customer service with dedicated RM",
            "Quarterly spa/wellness vouchers",
            "Golf course access (2 rounds/quarter)"
        ],
        "Color": "#FFD700"
    },
    {
        "Tier": "Luxe Platinum",
        "Eligibility": 2000000,
        "Points": 3,
        "Lounge Access": "Unlimited global",
        "Benefits": [
            "Personalized concierge",
            "Luxury brand invites",
            "Premium travel insurance"
        ],
        "Color": "#E5E4E2"
    },
    {
        "Tier": "Luxe Black",
        "Eligibility": "Invitation only",
        "Points": 4,
        "Lounge Access": "Unlimited global with VIP services",
        "Benefits": [
            "Exclusive events access",
            "Luxury travel packages",
            "Private jet booking assistance"
        ],
        "Color": "#000000"
    },
    {
        "Tier": "Luxe Ultra",
        "Eligibility": "Invitation only",
        "Points": 5,
        "Lounge Access": "Unlimited global with VIP services",
        "Benefits": [
            "Dedicated lifestyle manager",
            "Ultra-exclusive events",
            "Bespoke luxury experiences"
        ],
        "Color": "#1a237e"
    }
]

df = pd.DataFrame(tiers)

# Enhanced Streamlit App Styling
st.set_page_config(layout="wide", page_title="RuPay Luxe Rewards", page_icon="💎")

st.markdown("""
    <style>
        /* Global Styles */
        body {
            background-color: #0a192f;
            color: #e6f1ff;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        
        .stApp {
            background: linear-gradient(135deg, #0a192f 0%, #172a45 100%);
        }
        
        /* Header Styles */
        .main-header {
            background: linear-gradient(90deg, #1a237e 0%, #0d47a1 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #ffd700;
            text-align: center;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        /* Section Styles */
        .section-container {
            background: rgba(23, 42, 69, 0.7);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(230, 241, 255, 0.1);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .section-header {
            color: #ffd700;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            border-bottom: 2px solid rgba(255, 215, 0, 0.3);
            padding-bottom: 0.5rem;
        }
        
        /* Form Elements */
        .stSelectbox, .stNumberInput {
            background-color: #233554 !important;
            color: #e6f1ff !important;
            border-radius: 8px !important;
        }
        
        .stSlider {
            padding: 1rem 0;
        }
        
        /* Card Display */
        .card-tier {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Benefits List */
        .benefits-list {
            list-style-type: none;
            padding-left: 0;
        }
        
        .benefit-item {
            padding: 0.5rem 0;
            color: #e6f1ff;
            font-size: 0.9rem;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2rem;
            }
            
            .section-header {
                font-size: 1.2rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<div class="main-header"><h1 class="main-title">💎 RuPay Luxe Rewards Program</h1></div>', unsafe_allow_html=True)

# Create three columns for layout
col1, col2, col3 = st.columns([1, 1.2, 1])

# Column 1: User Profile
with col1:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">🧑‍💼 User Profile</h2>', unsafe_allow_html=True)
    
    existing_user = st.radio("Are you an existing RuPay Cardholder?", ["Yes", "No"])
    cibil_score = st.slider("Your CIBIL Score", 
                           min_value=300, 
                           max_value=900, 
                           value=750,
                           step=10,
                           help="Higher CIBIL score increases your chances of approval")
    
    card_experience = st.selectbox("Your experience with credit cards",
                                 ["Beginner", "Intermediate", "Expert"],
                                 help="Tell us about your credit card usage experience")
    
    occupation = st.selectbox("Occupation",
                            ["Salaried", "Self-employed", "Business Owner", "Professional"],
                            help="Select your primary occupation")
    
    annual_income = st.number_input("Annual Income (in ₹)",
                                  min_value=0,
                                  step=100000,
                                  help="Enter your annual income from all sources")
    st.markdown('</div>', unsafe_allow_html=True)

# Column 2: Eligibility Calculator
with col2:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">💰 Eligibility Calculator</h2>', unsafe_allow_html=True)
    
    annual_spending = st.number_input("Enter your annual spending (in ₹):",
                                    min_value=0,
                                    step=50000,
                                    help="Enter your estimated annual credit card spending")

    def calculate_eligibility(annual_spending, cibil_score, annual_income):
        eligible_cards = []
        for tier in tiers:
            eligibility_amount = tier["Eligibility"]
            if isinstance(eligibility_amount, str):
                continue
            
            if (annual_spending >= eligibility_amount and 
                cibil_score >= 650 and 
                annual_income >= eligibility_amount * 0.3):
                eligible_cards.append(tier)
        
        return eligible_cards

    eligible_cards = calculate_eligibility(annual_spending, cibil_score, annual_income)

    if eligible_cards:
        st.markdown("""
            <div style='background-color: rgba(0, 255, 0, 0.1); 
                        padding: 1rem; 
                        border-radius: 10px; 
                        border: 1px solid rgba(0, 255, 0, 0.3);
                        margin: 1rem 0;'>
                ✅ Based on your profile, you qualify for:
            </div>
        """, unsafe_allow_html=True)
        
        for card in eligible_cards:
            st.markdown(f"""
                <div class='card-tier' style='border-left: 4px solid {card["Color"]};'>
                    <h3 style='color: {card["Color"]};'>{card["Tier"]}</h3>
                    <p>Points per ₹100: {card["Points"]}</p>
                    <p>Lounge Access: {card["Lounge Access"]}</p>
                    <ul class='benefits-list'>
                        {"".join([f"<li class='benefit-item'>• {benefit}</li>" for benefit in card["Benefits"]])}
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No cards available for your current profile. Please review eligibility criteria.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Column 3: Program Details
with col3:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📌 Program Details</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style='color: #e6f1ff;'>
            <h3 style='color: #ffd700; font-size: 1.2rem;'>🎯 Core Benefits</h3>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li style='margin: 10px 0;'>• Personalized Rewards</li>
                <li style='margin: 10px 0;'>• Exclusive Access</li>
                <li style='margin: 10px 0;'>• High Reward Rates</li>
                <li style='margin: 10px 0;'>• Global Benefits</li>
            </ul>
            
            <h3 style='color: #ffd700; font-size: 1.2rem; margin-top: 20px;'>🚀 Accelerated Rewards</h3>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li style='margin: 10px 0;'>• 5x points - Luxury Retail</li>
                <li style='margin: 10px 0;'>• 3x points - Fine Dining</li>
                <li style='margin: 10px 0;'>• 4x points - Travel</li>
            </ul>
            
            <h3 style='color: #ffd700; font-size: 1.2rem; margin-top: 20px;'>🎁 Redemption Options</h3>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li style='margin: 10px 0;'>• Luxury Merchandise</li>
                <li style='margin: 10px 0;'>• Travel Benefits</li>
                <li style='margin: 10px 0;'>• Experiential Rewards</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; 
                padding: 1rem; 
                background: linear-gradient(90deg, #1a237e 0%, #0d47a1 100%);
                border-radius: 10px;
                margin-top: 2rem;'>
        <p style='color: #ffd700; margin: 0;'>
            Designed for the elite. Elevate your lifestyle with RuPay Luxe Rewards.
        </p>
        <p style='color: #e6f1ff; font-size: 0.8rem; margin-top: 0.5rem;'>
            © {datetime.now().year} RuPay Luxe. All rights reserved.
        </p>
    </div>
""", unsafe_allow_html=True)
