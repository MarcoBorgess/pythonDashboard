import streamlit as st
from controllers import bits, forge
from views import bitsCardList, forgeCardList

bitsTitleCol, forgeTitleCol = st.columns([1, 2])

with bitsTitleCol:
    st.title("Bits")
    
with forgeTitleCol:
    st.title("Forge")
    
bitsSelectCol, forgeSelectHotmCol, forgeSelectCostCol = st.columns([1, 1, 1])

with bitsSelectCol:
    rank = st.selectbox('Fame Rank', 
        ['New Player', 'Settler', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
        5
    )
    
with forgeSelectHotmCol:
    hotm = st.selectbox('HOTM Level', ['1', '2', '3', '4', '5', '6', '7'], 5)
    
with forgeSelectCostCol:
    maxCost = st.selectbox('Max Item Cost', ['1M', '10M', '100M'], 1)
    
bitsItemsCol, forgeItemsCol = st.columns([1, 2])

with bitsItemsCol:
    bitsItems = bitsCardList.getBitsCardList(bits.getBitsItems(), rank)
    st.markdown(bitsItems, unsafe_allow_html=True)

with forgeItemsCol:
    forgeItems = forgeCardList.getForgeCardList(forge.getSortedForgeItems(), hotm, maxCost)
    st.markdown(forgeItems, unsafe_allow_html=True)
