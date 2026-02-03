import streamlit as st
import pandas as pd
import joblib

# -------- CACHE FUNCTIONS --------
@st.cache_resource
def load_model():
    return joblib.load(
        "./pages/InsurancePricePrediction/xgboost_model_for_InsurancePrice_prediction.pkl"
    )

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

# -------- MAIN APP --------
def main():
    tab1, tab2 = st.tabs(["🔮 Predict Price", "📊 Data Analysis (EDA)"])
    file = "./pages/InsurancePricePrediction/insurance.csv"

    model = load_model()
    df = load_data(file)

    # -------- TAB 1: PREDICTION --------
    with tab1:
        st.title("Insurance Price Prediction Project")

        age = st.number_input("Enter Age : ", min_value=18)
        sex = st.selectbox("Select Gender : ", ['male', 'female'])
        bmi = st.number_input("Enter BMI : ", min_value=0.0)
        children = st.number_input("Enter Children Count : ", min_value=0)
        smoker = st.selectbox("You are Smoker ? : ", ['yes', 'no'])
        region = st.selectbox(
            "Select Region : ",
            ['northwest', 'northeast', 'southwest', 'southeast']
        )

        if st.button("Predict Insurance Price"):
            input_df = pd.DataFrame(
                [[age, sex, bmi, children, smoker, region]],
                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region']
            )

            price = round(model.predict(input_df)[0], 2)
            st.success(f"The predicted Insurance Price is : ${price}")

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
