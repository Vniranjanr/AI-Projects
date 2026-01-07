import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
import streamlit as st

st.set_page_config(
    page_title="AdventureWorks SQL Agent",
    layout="wide"
)

st.title("🧠 AdventureWorks SQL Assistant")
st.write("Ask questions about the AdventureWorks company database.")

# Load API key and setup OpenAI LLM
load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# SQL Server Connection
server = "localhost" 
database = "AdventureWorks2025" 
driver = "ODBC Driver 18 for SQL Server"
connection_string = (
    f"mssql+pyodbc://{server}/{database}?"
    f"driver={driver}&"
    "Trusted_Connection=yes&"
    "TrustServerCertificate=yes&"
    "Encrypt=yes"
)
engine = create_engine(connection_string)

# Define Tools
# 1. Tool to get table schema
@tool
def sqlserver_schema(table_name: str) -> str:
    """Get column names and data types for a SQL Server table. Input: Schema.Table"""
    query = text("""
        SELECT COLUMN_NAME, DATA_TYPE 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA + '.' + TABLE_NAME = :tname
    """)
    with engine.connect() as conn:
        rows = conn.execute(query, {"tname": table_name}).fetchall()
    return "\n".join([f"{row[0]} ({row[1]})" for row in rows]) if rows else "Not found."
# 2. Tool to execute SQL queries
@tool
def sqlserver_query(sql: str) -> str:
    """Execute a SQL Server query and return results. SQL Server syntax only."""
    with engine.connect() as conn:
        return str(conn.execute(text(sql)).fetchall())

# System Prompt
system_prompt = """You are an expert SQL Server analyst for AdventureWorks.
Always use fully qualified names (Schema.Table).
When asked about employees, give their names rather that IDs. 
Known schemas: HumanResources, Person, Sales, Production, Purchasing.
If you don't know the table names, query INFORMATION_SCHEMA.TABLES first."""

# Create the Agent 
agent = create_agent(
    model=llm, 
    tools=[sqlserver_schema, sqlserver_query],
    system_prompt=system_prompt
)

# Streamlit Interface
query = st.text_input("🔎 Enter your question:")

if st.button("Run Query", type="primary"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                result = agent.invoke(
                    {"messages": [("human", query)]}
                )
                answer = result["messages"][-1].content

                st.markdown("### ✅ Answer")
                st.write(answer)

            except Exception as e:
                st.error("Something went wrong:")
                st.exception(e)