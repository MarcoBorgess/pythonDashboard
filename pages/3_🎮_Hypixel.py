from calendar import c
import controller.globalController as globalController
import controller.itemsController as itemsController
import streamlit as st


globalController.setConfig()

rows = itemsController.getAllItems()
text = '# All items:\n'

# Print results.
count = 0
for row in rows:
    count+=1
    text += f"""<img src="{row[6]}" style="height: 16px;"> {row[3]} <br>"""
    if count > 10:
        break;

st.markdown(text, unsafe_allow_html=True)