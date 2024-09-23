import streamlit as st
from langchain_community.utilities import SQLDatabase


def connectDatabase(username, port, host, password, database):
    mysql_uri = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
    st.session_state.db = SQLDatabase.from_uri(mysql_uri)


def runQuery(query):
    return st.session_state.db.run(query) if st.session_state.db else "Please connect to database"


def getDatabaseSchema():
    return st.session_state.db.get_table_info() if st.session_state.db else "Please connect to database"