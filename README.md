# Simple Banking Chatbot with MySQL

A simple three-tier chatbot implementation with MySQL database integration.

## Features
- Natural language interface
- MySQL-backed knowledge base
- Basic intent recognition
- Banking domain focus (account information)

## Setup Instructions

1. **Prerequisites**:
   - Python 3.7+
   - MySQL Server

2. **Database Setup**:
   ```sql
   CREATE DATABASE chatbot_db;
   CREATE USER 'chatbot_user'@'localhost' IDENTIFIED BY 'chatbot_pass';
   GRANT ALL PRIVILEGES ON chatbot_db.* TO 'chatbot_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. **Installation**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Configuration**:
   Edit the `.env` file with your MySQL credentials

5. **Running**:
   ```bash
   python main.py
   ```

6. **Testing**:
   ```bash
   pytest
   ```