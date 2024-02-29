import pandas as pd
import streamlit as st
from catboost import CatBoostRegressor

st.set_page_config(layout="wide")


# Function to make predictions
def predict_salary(
    title,
    full_description,
    location,
    contract_type,
    contract_time,
    company,
    category,
    source_name,
):
    # Organize input data into a DataFrame
    data = {
        "Title": [title],
        "FullDescription": [full_description],
        "LocationNormalized": [location],
        "ContractType": [contract_type],
        "ContractTime": [contract_time],
        "Company": [company],
        "Category": [category],
        "SourceName": [source_name],
    }
    df = pd.DataFrame(data)

    # Load the trained model
    model = CatBoostRegressor()
    model.load_model("datalake/curated/model-v1.cbm")

    # Make prediction
    prediction = model.predict(df)

    return prediction[0]


# Streamlit Interface
def main():
    # Create two columns for layout
    col1, col2 = st.columns([1, 2])

    # Display summary on the left side
    with col1:
        st.title("Job Salary Prediction")
        st.markdown(
            """
            - **Exploratory Data Analysis (Data understanding):**
              - [[v1] - Exploratory Data Analysis/EDA (Data understanding)](https://github.com/drigols/jsp/blob/main/jsp/notebooks/eda.ipynb) # noqa: E501
            - **Training & Evaluation (Modeling & Evaluation):**
              - [[v1] - Training & Evaluation (baseline, dummy, PoC, prototype)](https://github.com/drigols/jsp/blob/main/jsp/notebooks/training-v1.ipynb)
            - **The current model uses the following features:**
              - **Independent variable:**
                - **Text Features:**
                  - Title
                  - FullDescription
                - **Categorical Features:**
                  - LocationNormalized
                  - ContractType
                  - ContractTime
                  - Company
                  - Category
                  - SourceName
              - **Dependent variable:**
                - SalaryNormalized
            - **Preprocessing:**
              - For the first training, I just trained the model without *preprocessing*.
              - That is because this is the "baseline (dummy, PoC, prototype)".
            - **The current model has an Evaluation Metric (MAE):**
              - 6.586
            - **Repository:** [Job Salary Prediction](https://github.com/drigols/jsp)
        """
        )

    # Collect user inputs on the right side
    with col2:
        st.header("Predict salary:")

        title = st.text_input("Title:")
        full_description = st.text_area("Full Description:")
        location = st.text_input("Location:")
        contract_type = st.selectbox(
            "Contract Type:",
            [
                "Full Time",
                "Part Time",
            ],
        )
        contract_time = st.selectbox(
            "Contract Time:", ["Permanent", "Contract"]
        )
        company = st.text_input("Company:")
        category = st.text_input("Category:")
        source_name = st.text_input("Source Name:")

        # Predict button.
        if st.button("Make Prediction"):
            prediction = predict_salary(
                title,
                full_description,
                location,
                contract_type,
                contract_time,
                company,
                category,
                source_name,
            )
            st.success(
                f"The predicted salary is: {prediction:,.0f}".replace(",", ".")
            )


if __name__ == "__main__":
    main()
