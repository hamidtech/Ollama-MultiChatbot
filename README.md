# Ollama-MultiChatbot

![Streamlit](https://img.shields.io/badge/Streamlit-✓-blue) ![Python](https://img.shields.io/badge/Python-✓-blue)![Ollama](https://img.shields.io/badge/Ollama-✓-green)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub stars](https://img.shields.io/github/stars/hamidtech/Ollama-MultiChatbot?style=social)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to the **Ollama-MultiChatbot** project! This application provides an interactive web interface that allows users to interact with a MySQL database, process PDFs, and engage in free-form conversations using natural language queries. By leveraging Streamlit for the frontend and LangChain integrated with the ChatOllama language model, the application translates plain English questions into actionable commands, executes them, and returns the results in an easy-to-understand format.

## Features

- **Natural Language Processing:** Input queries in everyday language, which are converted into SQL statements or PDF processing commands by the language model.
- **Interactive Chat Interface:** Seamless conversation with the system, maintaining chat history for context.
- **Dynamic Database Connection:** Connect to any MySQL database by entering your credentials through the sidebar.
- **PDF Processing:** Upload and interact with PDF documents using natural language commands.
- **Automated Response Generation:** Executes queries and processes results or PDF content, translating them back into human-readable responses.
- **Session Management:** Maintains state across user interactions to ensure a smooth user experience.

## Technologies Used

- **[Streamlit](https://streamlit.io/):** For building the interactive web application.
- **[LangChain](https://github.com/hwchase17/langchain):** To integrate the language model for interpreting and generating SQL queries and PDF processing commands.
- **[MySQL](https://www.mysql.com/):** As the relational database management system.
- **[ChatOllama (LLM)](https://github.com/langchain-community/langchain-llm):** For processing natural language inputs and producing corresponding SQL queries or PDF commands.
- **[Python 3.7+](https://www.python.org/):** Programming language used for development.

## Installation

Follow these steps to set up and run the application locally.

### Prerequisites

- **Python 3.7 or higher** installed on your machine.
- **MySQL Server** running and accessible.
- **Git** installed to clone the repository.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/hamidtech/Ollama-MultiChatbot.git
   cd Ollama-MultiChatbot
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

   *If a `requirements.txt` file is not present, you can install the necessary packages directly:*

   ```bash
   pip install streamlit langchain_community mysql-connector-python
   ```

4. **Set Up Environment Variables (Optional but Recommended)**

   To securely manage database credentials, consider using environment variables or a `.env` file.

   ```bash
   touch .env
   ```

   Add the following to the `.env` file:

   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_USERNAME=root
   DB_PASSWORD=yourpassword
   DB_NAME=music
   ```

   *Ensure you update the values with your actual database credentials.*

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   *Replace `your_app.py` with the actual name of your Python script.*

## Usage

1. **Connect to the Database**

   - Open the application in your browser (usually at `http://localhost:8501`).
   - In the sidebar, enter your MySQL database credentials:
     - **Host**
     - **Port**
     - **Username**
     - **Password**
     - **Database Name**
   - Click the **Connect** button. A success message will appear upon a successful connection.

2. **Interact via Chat**

   - Use the chat input at the bottom of the page to enter your natural language queries.
   - Example Queries:
     - "How many albums are in the database?"
     - "List all customers from Brazil."
     - "Summarize the contents of the uploaded PDF."
   - The application will display both your query and the assistant's response.

## Database Setup

To set up the necessary database schema and populate it with sample data, execute the provided SQL scripts in MySQL environment.

Use any public MySQL environemnt like MySQL Workbench to run .sql file

*Ensure you replace `yourusername` and `yourpassword` with your actual MySQL credentials.*

## Contributing

Contributions are welcome! If you'd like to enhance this project, please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to reach out:

- **Hamid Jamali**
- **Email:** [hamid1375jamali@gmail.com](mailto:hamid1375jamali@gmail.com)
- **GitHub:** [hamidtech](https://github.com/hamidtech)
