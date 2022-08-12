import streamlit as st
from controllers import f1API, items
from views import defaultStyle
from time import sleep

defaultStyle.setConfig()

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
        placeholder.text(f1API.updateF1())
        sleep(3)
        placeholder.empty()
        
def UpdateForge():
    forgeItems = items.getForgeItemsIds()
    st.text("🟢 -> Ativado | 🔴 -> Desativado")
    
    def formatName(forgeItem):
        if (forgeItem.active == 1):
            return f'🟢 {forgeItem.name}'
    
        return f'🔴 {forgeItem.name}'
    
    formatedList = [formatName(forgeItem) for forgeItem in forgeItems]
    
    selectedItem = st.selectbox("Select an item", formatedList, 0)
    if (selectedItem.startswith("🟢")):
        desativar = st.button("❌ Desativar")
        if (desativar):
            success = items.updateForgeItemActive(forgeItems[formatedList.index(selectedItem)]['idHypixel'], 0)
            if (success):
                st.success("Item desativado!")
                sleep(1)
                st.experimental_rerun()
    else:
        ativar = st.button("✔️ Ativar")
        if (ativar):
            success = items.updateForgeItemActive(forgeItems[formatedList.index(selectedItem)]['idHypixel'], 1)
            if (success):
                st.success("Item ativado!")
                sleep(1)
                st.experimental_rerun()
   
if check_password():
    UpdateF1()
    UpdateForge()