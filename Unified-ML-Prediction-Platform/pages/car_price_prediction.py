import streamlit as st
import pandas as pd
import joblib
import os
# -------- CACHE FUNCTIONS --------
@st.cache_resource
def load_model():
    # Folder ka naam beech mein add kiya hai
    path = os.path.join(os.path.dirname(__file__), "Car_Price_Prediction", "final_random_forest_model.pkl")
    return joblib.load(path)

@st.cache_data
def load_data():
    path = os.path.join(os.path.dirname(__file__), "Car_Price_Prediction", "car_price_cleaned_data.csv")
    return pd.read_csv(path)

# -------- MAIN APP --------
def main():
    tab1, tab2 = st.tabs(["🔮 Predict Price", "📊 Data Analysis (EDA)"])
    file = "./pages/Car_Price_Prediction/car_price_cleaned_data.csv"

    # Load once
    model = load_model()
    df = load_data()

    # -------- TAB 1: PREDICTION --------
    with tab1:
        st.title("Car Price Prediction Project")

        levy = st.number_input("Enter the car's levy:", min_value=0.0)
        manufacturer = st.selectbox("Select Manufacturer:", df['Manufacturer'].unique())
        model_name = st.selectbox("Select Model:", df['Model'].unique())
        prod_year = st.selectbox("Select Production Year:", sorted(df['Prod. year'].unique()))
        category = st.selectbox("Select Category:", sorted(df['Category'].unique()))
        leather_interior = st.selectbox("Leather Interior (Yes/No):", ['Yes', 'No'])
        fuel_type = st.selectbox("Select Fuel Type:", sorted(df['Fuel type'].unique()))
        engine_volume = st.number_input("Enter Engine Volume (in liters):", min_value=0.0)
        mileage = st.number_input("Enter Mileage (in km):", min_value=0)
        cylinders = st.selectbox("Select Number of Cylinders:", sorted(df['Cylinders'].unique()))
        gear_box_type = st.selectbox("Select Gear Box Type:", sorted(df['Gear box type'].unique()))
        drive_wheels = st.selectbox("Select Drive Wheels:", sorted(df['Drive wheels'].unique()))
        doors = st.selectbox("Select Number of Doors:", sorted(df['Doors'].unique()))
        wheel = st.selectbox("Select Wheel Type:", sorted(df['Wheel'].unique()))
        color = st.selectbox("Select Color:", sorted(df['Color'].unique()))
        airbags = st.selectbox("Select Number of Airbags:", sorted(df['Airbags'].unique()))
        turbo = st.selectbox("Turbo (Yes/No):", [0, 1])

        if st.button("Predict Car Price"):
            input_data = pd.DataFrame(
                [[
                    levy, manufacturer, model_name, prod_year, category,
                    leather_interior, fuel_type, engine_volume, mileage,
                    cylinders, gear_box_type, drive_wheels, doors,
                    wheel, color, airbags, turbo
                ]],
                columns=[
                    'Levy', 'Manufacturer', 'Model', 'Prod. year', 'Category',
                    'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
                    'Cylinders', 'Gear box type', 'Drive wheels', 'Doors',
                    'Wheel', 'Color', 'Airbags', 'Turbo'
                ]
            )

            prediction = model.predict(input_data)[0]
            st.success(f"The predicted car price is: ${round(prediction, 2)}")

    # -------- TAB 2: EDA --------
    with tab2:
        st.title("Exploratory Data Analysis (EDA)")
        st.dataframe(df.head(10))

        if st.checkbox("Show Summary Statistics"):
            st.write(df.describe())

        if st.checkbox("Show Value Counts for Categorical Columns"):
            categorical_cols = df.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                st.write(f"Value counts for {col}:")
                st.write(df[col].value_counts())

if __name__ == "__main__":
    main()
