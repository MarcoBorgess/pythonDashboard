import controller.globalController as globalController
import streamlit as st
import controller.f1Requests as f1api
from time import sleep

globalController.setConfig()

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

# UpdateButton
def UpdateF1():
    updateButton = st.button("Update F1")
    placeholder = st.empty()
    if updateButton:
        placeholder.text(f1api.updateF1())
        sleep(3)
        placeholder.empty()

if check_password():
    UpdateF1()