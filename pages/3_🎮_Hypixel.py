import streamlit as st
from controllers import bits, forge
from views import bitsCardList, defaultStyle

defaultStyle.setConfig()

bitsCol, forgeCol, katCol = st.columns(3)

with bitsCol:
    st.title('Bits')
    rank = st.selectbox('Fame Rank', 
                ['New Player', 'Settler', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
                5
                )
    bitsItems = bitsCardList.getBitsWidget(bits.getBitsItems(), rank)
    st.markdown(bitsItems, unsafe_allow_html=True)

with forgeCol:
    st.title('Forge')
    # rank = st.selectbox('HOTM Level', 
    #             ['1', '2', '3', '4', '5', '6', '7'],
    #             5
    #             )
    # forgeItems = bitsItemsWidget.getBitsWidget(bitsController.getBitsItems(), rank)
    # st.markdown(forgeItems, unsafe_allow_html=True)
    forgeItems = forge.getForgeItems()
    for item in forgeItems:
        st.write(item)

with katCol:
    st.title('Kat')
    # rank = st.selectbox('Taming Level', 
    #             ['New Player', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
    #             5
    #             )
    # katItems = bitsItemsWidget.getBitsWidget(bitsController.getBitsItems(), rank)
    # st.markdown(katItems, unsafe_allow_html=True)
    
