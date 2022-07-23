from calendar import c
import controller.globalController as globalController
import controller.itemsController as itemsController
import streamlit as st


globalController.setConfig()

rows = itemsController.getBitsItems()
text = '# Bits items:\n'

# Print results.
for row in rows:
    text += f"""<img src="{row[4]}" style="height: 16px;"> {row[1]} <br>"""

st.markdown(text, unsafe_allow_html=True)