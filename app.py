import streamlit as st
from database import connectDatabase , runQuery 
from llmtemplate import getQueryFromLLM , getResponseForQueryResult 





st.set_page_config(
    page_icon="🤖",
    page_title="Chat with MYSQL - Hamid :)",
    layout="centered"
)

question = st.chat_input('Start ask database :)')

if "chat" not in st.session_state:
    st.session_state.chat = []

if question:
    if "db" not in st.session_state:
        st.error('Please connect database first.')
    else:
        st.session_state.chat.append({
            "role": "user",
            "content": question
        })

        query = getQueryFromLLM(question)
        print(query)
        result = runQuery(query)
        print(result)
        response = getResponseForQueryResult(question, query, result)
        st.session_state.chat.append({
            "role": "assistant",
            "content": response
        })

for chat in st.session_state.chat:
    st.chat_message(chat['role']).markdown(chat['content'])

with st.sidebar:
    st.title('Connect to MYSQL database')
    st.text_input(label="Host", key="host", value="localhost")
    st.text_input(label="Port", key="port", value="3306")
    st.text_input(label="Username", key="username", value="root")
    st.text_input(label="Password", key="password", value="", type="password")
    st.text_input(label="Database", key="database", value="music")
    connectBtn = st.button("Connect")
    st.header("AI class Project :)")
    st.header("Modified by Hamid Jamali")


if connectBtn:
    connectDatabase(
        username=st.session_state.username,
        port=st.session_state.port,
        host=st.session_state.host,
        password=st.session_state.password,
        database=st.session_state.database,
    )

    st.success("Database connected")

