import streamlit as st
import mysql.connector

def insertItem(newItemId, newParams):
    @st.experimental_singleton
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])
        
    conn = init_connection()

    # Perform query.
    # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
    @st.experimental_memo
    def run_query(query):
        with conn.cursor() as cur:
            queryString = str(query).replace('{', '').replace('}', '')
            print('QUERY: '+ queryString)
            cur.execute(queryString)
            conn.commit()
            return 'OK'

    
    result = run_query(f"INSERT INTO bins (itemId, params) VALUES({newItemId}, {newParams})")
    
    return f'Inserted {newItemId}{newParams} into Bins ({result})'

