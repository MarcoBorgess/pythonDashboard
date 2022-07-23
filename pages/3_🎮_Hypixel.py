from controller import globalController, bitsController
from widgets import bitsItemsWidget
import streamlit as st


globalController.setConfig()

bits, kat, forge = st.columns(3)

with bits:
    st.title('Bits')
    rank = st.selectbox('Fame Rank', 
                ['New Player', 'Settler', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
                5
                )
    bitsItems = bitsItemsWidget.getBitsWidget(bitsController.getBitsItems(), rank)
    st.markdown(bitsItems, unsafe_allow_html=True)
    
with kat:
    st.title('Kat')
    # rank = st.selectbox('Taming Level', 
    #             ['New Player', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
    #             5
    #             )
    # katItems = bitsItemsWidget.getBitsWidget(bitsController.getBitsItems(), rank)
    # st.markdown(katItems, unsafe_allow_html=True)
    
with forge:
    st.title('Forge')
    # rank = st.selectbox('HOTM Level', 
    #             ['Settler', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
    #             5
    #             )
    # forgeItems = bitsItemsWidget.getBitsWidget(bitsController.getBitsItems(), rank)
    # st.markdown(forgeItems, unsafe_allow_html=True)