from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from database import getDatabaseSchema 

llm = ChatOllama(model="llama3.1")

def getQueryFromLLM(question):
    template = """below is the schema of MYSQL database, read the schema carefully about the table and column names. Also take care of table or column name case sensitivity.
    Finally answer user's question in the form of SQL query.

    {schema}

    please only provide the SQL query and nothing else

    for example:
    question: how many albums we have in database
    SQL query: SELECT COUNT(*) FROM album
    question: how many customers are from Brazil in the database ?
    SQL query: SELECT COUNT(*) FROM customer WHERE country=Brazil

    your turn :
    question: {question}
    SQL query :
    please only provide the SQL query and nothing else
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "schema": getDatabaseSchema()
    })
    return response.content


def getResponseForQueryResult(question, query, result):
    template2 = """below is the schema of MYSQL database, read the schema carefully about the table and column names of each table.
    Also look into the conversation if available
    Finally write a response in natural language by looking into the conversation and result.

    {schema}

    Here are some example for you:
    question: how many albums we have in database
    SQL query: SELECT COUNT(*) FROM album;
    Result : [(34,)]
    Response: There are 34 albums in the database.

    question: how many users we have in database
    SQL query: SELECT COUNT(*) FROM customer;
    Result : [(59,)]
    Response: There are 59 amazing users in the database.

    question: how many users above are from india we have in database
    SQL query: SELECT COUNT(*) FROM customer WHERE country=india;
    Result : [(4,)]
    Response: There are 4 amazing users in the database.

    your turn to write response in natural language from the given result :
    question: {question}
    SQL query : {query}
    Result : {result}
    Response:
    """

    prompt2 = ChatPromptTemplate.from_template(template2)
    chain2 = prompt2 | llm
    
    response = chain2.invoke({
        "question": question,
        "schema": getDatabaseSchema(),
        "query": query,
        "result": result
    })
    return response.content