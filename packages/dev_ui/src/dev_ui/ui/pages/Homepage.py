import streamlit as st
from dev_ui.ui.pages.GrossNetPage import render_page as render_gross_net
from dev_ui.ui.pages.UploadFilesPage import render_page as render_upload_files

st.sidebar.title("CAT Salary Tools")
page = st.sidebar.selectbox("Choose a page", ["Gross-Net", "Upload Files"])

if page == "Gross-Net":
    render_gross_net()
elif page == "Upload Files":
    render_upload_files()
