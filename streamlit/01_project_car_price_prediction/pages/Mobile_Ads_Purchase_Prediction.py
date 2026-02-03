import streamlit as st
import pandas as pd
import joblib
import os
# ---------- CACHE FUNCTIONS ----------
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "xgboost_model.pkl")
    return joblib.load(model_path)

@st.cache_data
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), "cleaned_mobile_dataset.csv")
    return pd.read_csv(csv_path)

# ---------- MAIN APP ----------
def main():
    tab1, tab2 = st.tabs(["🔮 Predict Price", "📊 Data Analysis (EDA)"])
    # Load once
    model = load_model()
    df = load_data()

    # ---------- TAB 1 ----------
    with tab1:
        st.title("Mobile Ads Purchase Prediction Project")

        Gender = st.selectbox("Select Gender : ", ['Male', 'Female'])
        Age = st.number_input("Enter Age:", min_value=18)
        EstimatedSalary = st.number_input("Enter Estimated Salary:", min_value=0)

        if st.button("Predict Purchase"):
            input_data = pd.DataFrame(
                [[Gender, Age, EstimatedSalary]],
                columns=['Gender', 'Age', 'EstimatedSalary']
            )

            prediction = model.predict(input_data)

            result = "Will Purchase the Mobile" if prediction[0] == 1 else "Will Not Purchase the Mobile"
            st.success(f"The predicted result is: {result}")

    # ---------- TAB 2 ----------
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
