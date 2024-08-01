from dotenv import load_dotenv
load_dotenv()  # loads all the env variables

import streamlit as st
from PIL import Image
import os
import pandas as pd
import sqlite3

import google.generativeai as genai
## configure genai key

api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key: {api_key}")  # Debug print
if not api_key:
    st.error("API key is missing. Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

## function to load Google Gemini Model and get queries

def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content([prompt[0], question])
        print(f"Gemini Response: {response.text}")  # Debug print
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        st.error(f"Error generating response: {e}")
        return ""

## function to retrieve query from the database

def read_sql_query(sql, db):
    try:
        print(f"Executing SQL: {sql}")  # Debug print
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        columns = [description[0] for description in cur.description]
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        for row in rows:
            print(row)
        conn.close()
        return df
    except Exception as e:
        print(f"Error executing SQL: {e}")
        st.error(f"Error executing SQL: {e}")
        return []

## define your prompt
prompt = [
"""
You are an expert in converting the English questions to SQL query!
The SQL database has the name Account and has the following columns - ['CustomerID', 'AccountType', 'AccountBalance', 'DateOfAccountOpening', 'LastTransactionDate', 'AccountID'] \n\n 
For example, \n Example 1 - How many entries of records are present?,
the sql command will be like SELECT COUNT(*) FROM ACCOUNT;
\n Example 2 - How many customers have savings account?,
the SQL command will be something like this SELECT COUNT(*) FROM Account WHERE AccountType="Savings"
also sql code should not have ''' in beginning or in the end and sql word in the output
"""
]  ## in context learning with few shot inference

## streamlit app

st.set_page_config(page_title="Retrieve any SQL query",page_icon="💻")
st.markdown(
    """
    <h1 style="
        background-color: #A8E4E4;
        color: #333;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    ">
        QueryBot: Language to SQL
    </h1>
    """,
    unsafe_allow_html=True
)

# Input box for the question
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## if submitted
if submit:
    print("Button clicked")  # Debug print
    geminiresponse = get_gemini_response(question, prompt)
    print(f"Generated SQL: {geminiresponse}")  # Debug print
    if geminiresponse:
        sqlresponse = read_sql_query(geminiresponse, "banking.db")
        st.subheader("The response is")
        #df = pd.DataFrame(sqlresponse)
        st.dataframe(sqlresponse)
