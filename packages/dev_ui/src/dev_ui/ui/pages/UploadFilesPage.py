import streamlit as st
import pandas as pd
import requests

API_URL = "http://backend:8000/net-ease/calculate"

def render_page():
    st.header("📁 Upload Employee Salary Sheet")

    uploaded_file = st.file_uploader("Upload your file (CSV or Excel)", type=["csv", "xlsx"])
    
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return

        # Check required columns
        required_cols = {"Gross Salary", "Number of Dependents"}
        if not required_cols.issubset(df.columns):
            st.error("Missing required columns: Gross Salary and Number of Dependents")
            return

        # Calculate net salary for each row
        net_salaries = []
        for _, row in df.iterrows():
            try:
                response = requests.get(API_URL, json={
                    "gross_salary": int(row["Gross Salary"]),
                    "number_of_dependents": int(row["Number of Dependents"])
                })
                if response.ok:
                    result = response.json()
                    net_salaries.append(result["net_salary"])
                else:
                    net_salaries.append("ERROR")
            except Exception as e:
                net_salaries.append("ERROR")

        df["Net Salary"] = net_salaries
        st.success("Net salaries calculated!")
        st.dataframe(df)

        # Optionally allow download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results as CSV", data=csv, file_name="net_salaries.csv", mime="text/csv")
