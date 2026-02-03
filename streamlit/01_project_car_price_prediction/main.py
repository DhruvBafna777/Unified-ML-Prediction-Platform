import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI Prediction Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS to hide default header and footer for cleaner look
hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Sidebar (Optional but looks professional)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100) # Placeholder logo
    st.title("Navigation")
    st.info("Select a model from the dashboard to start predicting.")
    st.markdown("---")
    st.markdown("Created with ❤️ by Dhruv Bafna")

# 4. Hero Section
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 ML Prediction Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Welcome to your centralized Machine Learning Dashboard. Select a domain below to get started.</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. Model Selection Grid
col1, col2, col3, col4 = st.columns(4, gap="medium")

# Card 1: Car Price
with col1:
    with st.container(border=True): # Creates a box/card effect
        st.markdown("<h1 style='text-align: center;'>🚗</h1>", unsafe_allow_html=True)
        st.subheader("Car Price Prediction")
        st.write("Estimate the market value of used cars based on specifications like mileage, year, and brand.")
        st.markdown("###") # Spacer
        if st.button("Launch Tool ➜", key="car_btn", use_container_width=True):
            st.switch_page("pages/Car_Price_Prediction/car_price_prediction.py")

# Card 2: Mobile Ads
with col2:
    with st.container(border=True):
        st.markdown("<h1 style='text-align: center;'>📱</h1>", unsafe_allow_html=True)
        st.subheader("Ad Purchase Predictor")
        st.write("Analyze user behavior to predict if a user will purchase a product after clicking an ad.")
        st.markdown("###") # Spacer
        if st.button("Launch Tool ➜", key="mobile_btn", use_container_width=True):
            st.switch_page("pages/Mobile_Ads_Purchase_Prediction/Mobile_Ads_Purchase_Prediction.py")

# Card 3: House Price
with col3:
    with st.container(border=True):
        st.markdown("<h1 style='text-align: center;'>🏥</h1>", unsafe_allow_html=True)
        st.subheader("Insurance Price Prediction")
        st.write("Predict insurance costs based on personal and demographic information.")
        st.markdown("###") # Spacer
        if st.button("Launch Tool ➜", key="insurance_btn", use_container_width=True):
            st.switch_page("pages/InsurancePricePrediction/Insurance_price_Prediction.py")
            
with col4:
    with st.container(border=True):
        st.markdown("<h1 style='text-align: center;'>💎</h1>", unsafe_allow_html=True)
        st.subheader("Diamonds Price Prediction")
        st.write("Estimate the price of diamonds based on their characteristics like carat, cut, color, and clarity.")
        st.markdown("###") # Spacer
        if st.button("Launch Tool ➜", key="diamonds_btn", use_container_width=True):
            st.switch_page("pages/Diamonds_price_prediction/Diamonds_price_prediction.py")

# Footer area
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2025 Dhruv Bafna.</p>", unsafe_allow_html=True)
