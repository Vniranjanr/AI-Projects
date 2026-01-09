# 🤖 SQL Server Agentic AI

> An intelligent agentic system that autonomously interacts with SQL Server databases using natural language, powered by OpenAI and Langchain.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-1.2-green.svg)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-gpt_4o-purple.svg)](https://www.anthropic.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-yellow.svg)](LICENSE)

## 📋 Overview

This project demonstrates an advanced **agentic AI architecture** that enables natural language database interactions. Built with Langchain and Claude AI, the system autonomously generates SQL queries, executes them against SQL Server databases, and provides intelligent responses to complex data questions.

### Key Highlights

- **🎯 Autonomous Decision-Making**: Agent intelligently decides when to query the database vs. provide direct answers
- **🔄 Self-Correcting**: Automatically handles errors and refines queries for accurate results
- **💬 Natural Language Interface**: Ask questions in plain English, get precise data insights
- **🏗️ Production-Ready Architecture**: Built with Langchain for robust, stateful workflow management
- **🔐 Secure**: Implements best practices for database access and API key management

## 🏗️ Architecture

![Workflow](../images/workflow.png)

The system uses a sophisticated agent loop that:
1. Analyzes user questions and database schema
2. Generates optimized SQL queries
3. Executes queries safely with error handling
4. Processes results and formats human-readable responses
5. Iterates until query goals are achieved

## 🛠️ Technical Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **LangChain/Langchain** | Agent orchestration and workflow management |
| **OpenAI** | Natural language understanding and SQL generation |
| **pyodbc** | SQL Server database connectivity |
| **dotenv** | Environment configuration management |

## ✨ Features

### Core Capabilities
- **Natural Language to SQL**: Translates complex questions into optimized SQL queries
- **Schema-Aware**: Understands database structure for accurate query generation
- **Multi-Turn Conversations**: Maintains context across multiple questions
- **Error Recovery**: Automatically debugs and fixes SQL errors
- **Result Synthesis**: Converts raw data into meaningful insights

## 🎯 Key Skills Demonstrated

- **AI/ML Engineering**: Implementing production-grade agentic AI systems
- **LangChain/Langchain**: Building stateful, multi-step AI workflows
- **Database Engineering**: SQL Server integration and query optimization
- **Python Development**: Clean, maintainable code with best practices
- **System Design**: Architecting autonomous, error-resilient systems
- **API Integration**: Working with modern LLM APIs 
  
## 🚀 Getting Started

### Prerequisites

```bash
# System Requirements
- Python 3.8 or higher
- SQL Server (local or remote instance)
- ODBC Driver for SQL Server
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vniranjanr/AI-Projects.git
   cd AI-Projects/SQLServer_AgenticAI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Create .env file
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Update database configuration**
   
   Edit the connection string in the code to point to your SQL Server instance.

### Quick Start

```python
# Run the agent
stremlit run main.py

# Example queries:
# "How many employees are in the Sales department?"
# "What's the average salary by department?"
# "Show me the top 5 highest-paid employees"
```

## 📊 Use Cases

This agentic system excels at:

- **Business Intelligence**: "What were our top-selling products last quarter?"
- **Data Analysis**: "Compare revenue trends across regions"
- **Reporting**: "Generate a summary of customer demographics"
- **Data Exploration**: "What tables contain customer information?"
- **Troubleshooting**: "Find all orders with missing shipment dates"


## 📁 Project Structure

```
SQLServer_AgenticAI/
├── main.py                 # Main application entry point
├── agent.py               # Langchain agent implementation
├── database.py            # SQL Server connection and utilities
├── prompts.py             # System prompts and templates
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🔮 Future Enhancements

- [ ] Multi-database support (PostgreSQL, MySQL, etc.)
- [ ] Query result caching for improved performance
- [ ] Web interface for non-technical users
- [ ] Advanced analytics and visualization generation
- [ ] Query history and audit logging
- [ ] Role-based access control
- [ ] Streaming responses for large result sets

## 📝 Example Interaction


## 👨‍💻 Author

**Niranjan**

- GitHub: [@Vniranjanr](https://github.com/Vniranjanr)
- LinkedIn: [Connect with me](https://linkedin.com/in/yourprofile)

