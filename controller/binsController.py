import streamlit as st
import mysql.connector

def insertItem(newItemId, newParams):
    @st.experimental_singleton
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])

    def run_query(query):
        conn = init_connection()
        with conn.cursor() as cur:
            queryString = str(query).replace('{', '').replace('}', '')
            print('QUERY: '+ queryString)
            cur.execute(queryString)
            conn.commit()
            cur.close()
            conn.close()
            return 'OK'

    
    result = run_query(f"INSERT INTO bins (itemId, params) VALUES({newItemId}, {newParams})")
    
    return f'Inserted {newItemId}{newParams} into Bins ({result})'

