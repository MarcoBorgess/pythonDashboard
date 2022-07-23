import streamlit as st
import mysql.connector


@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo
def run_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def getBitsItems():
    rows = run_query(
        """
            SELECT item.idHypixel, name, rarity, category, iconURL, npcSellPrice, bits, bz, ah, item.updatedOn as itemUpdatedOn,
                bin, secondBin, ah.updatedOn as ahUpdatedOn,
                sellPrice, buyPrice, sellVolume, buyVolume, sellMovingWeek, buyMovingWeek, sellOrders, buyOrders, bz.updatedon as bzUpdatedOn
            FROM item
            LEFT JOIN ah ON ah.idHypixel = item.idHypixel
            LEFT JOIN bz ON bz.idHypixel = item.idHypixel
            WHERE bits > 0
        """
    )
    return rows