import streamlit as st
import pandas as pd
import joblib
import seaborn as sns 
import os

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "final_xgboost_model_for_diamonds.pkl")
    return joblib.load(model_path)
    
@st.cache_data
def load_data():
    return sns.load_dataset('diamonds')

def main():
    tab1, tab2 = st.tabs(["🔮 Predict Price", "📊 Data Analysis (EDA)"])

    model = load_model()
    df = load_data()

    with tab1:
        st.title("Diamonds Price Prediction Project")

        carat = st.number_input("Enter the carat weight of the diamond:", min_value=0.0, format="%.2f")
        cut = st.selectbox("Select Cut Quality:", sorted(df['cut'].unique()))
        color = st.selectbox("Select Color Grade:", sorted(df['color'].unique()))
        clarity = st.selectbox("Select Clarity Grade:", sorted(df['clarity'].unique()))
        depth = st.number_input("Enter Depth Percentage:", min_value=0.0, format="%.2f")
        table = st.number_input("Enter Table Percentage:", min_value=0.0, format="%.2f")
        x_length = st.number_input("Enter Length (mm):", min_value=0.0, format="%.2f")
        y_width = st.number_input("Enter Width (mm):", min_value=0.0, format="%.2f")
        z_depth = st.number_input("Enter Depth (mm):", min_value=0.0, format="%.2f")

        if st.button("Predict Diamond Price"):
            input_data = pd.DataFrame(
                [[
                    carat, cut, color, clarity,
                    depth, table, x_length, y_width, z_depth
                ]],
                columns=[
                    'carat', 'cut', 'color', 'clarity',
                    'depth', 'table', 'x_length', 'y_width', 'z_depth'
                ]
            )

            prediction = model.predict(input_data)
            st.success(f"The predicted price of the diamond is: ${prediction[0]:,.2f}")

    with tab2:
        st.title("Exploratory Data Analysis (EDA) on Diamonds Dataset")
        st.dataframe(df.head())

        st.subheader("Price Distribution")
        st.bar_chart(df['price'].value_counts().head(20))

        st.subheader("Carat vs Price")
        st.line_chart(df.groupby('carat')['price'].mean())
        
if __name__ == "__main__":
    main()
