### packages/dev_ui/src/dev_ui/ui/pages/💬_Gross_Net.py
import streamlit as st
import requests

API_URL = "http://localhost:8000/net-ease/calculate"

def render_page():
    st.header("Gross → Net Salary Calculator")
    gross = st.number_input("Gross Salary (VND)", min_value=0, step=100000)
    dependents = st.number_input("Number of Dependents", min_value=0, step=1)

    if st.button("Calculate"):
        response = requests.get(API_URL, json={
            "gross_salary": gross,
            "number_of_dependents": dependents
        })
        if response.ok:
            data = response.json()
            st.success(f"Net Salary: {data['net_salary']:,} VND")
            st.write("Breakdown:")
            st.json(data)
        else:
            st.error("Failed to calculate net salary.")
