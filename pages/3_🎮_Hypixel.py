import controller.globalController as globalController
import controller.itemsController as itemsController
import streamlit as st


globalController.setConfig()

rows = itemsController.getAllItems()
text = '# All items:\n'

# Print results.
for row in rows:
    text += f"""<img src="{row[6]}" style="height: 16px;"> {row[3]} <br>"""

st.markdown(text, unsafe_allow_html=True)