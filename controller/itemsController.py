import streamlit as st
import mysql.connector

def getAllItems():
    @st.experimental_singleton
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])

    conn = init_connection()

    # Perform query.
    # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
    @st.experimental_memo
    def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    rows = run_query("SELECT * from iteminfo;")
    return rows