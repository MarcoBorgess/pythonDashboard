import streamlit as st

def setConfig():
    st.set_page_config(
        page_title="Marco",
        page_icon="house",
        layout="wide", 
    )

    # Sidebar width
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 150px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 150px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )