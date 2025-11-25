Room Service Agent – AI/ML Assignment

Project Overview:
This project implements a Room Service Assistant that processes natural language food orders, handles dietary preferences, asks clarifying questions, stores conversation history, and manages basic hospitality logic. It uses Python, FastAPI, MongoDB, and a Mock LLM.

Tech Stack:
Python
FastAPI
MongoDB
Motor (async driver)
Uvicorn
Mock LLM

Project Structure:
room-service-agent/
service/app.py - API endpoints
service/agent.py - Agent logic
service/db.py - MongoDB connection
service/llm_adapter.py - Mock LLM
seed.py - Seed menu
check_db.py - DB test
requirements.txt
.env
.env.example
README.txt

Setup Instructions:
1. Install dependencies:
pip install -r requirements.txt

2. Start MongoDB (Docker):
docker run -d --name room_mongo -p 27017:27017 -v room_mongo_data:/data/db mongo:6.0

3. Seed data:
python seed.py

4. Run server:
uvicorn service.app:app --reload --port 8000

API Endpoints:
POST /register
POST /message

Agent Logic:
Fetch or create guest.
Store conversation.
Match menu items.
Use mock LLM for ambiguity.
Confirm order.

Conversation Examples:
User: I want pasta or pizza
Agent: Can you clarify your choice?

User: I want pasta
Agent: We have gluten-free pasta and salad. Which would you like?

User: I want a vegetarian burger
Agent: The chicken burger conflicts with vegetarian preference.

User: Can I get noodles?
Agent: Could you please clarify your order?

Future Improvements:
Real LLM integration
Better menu matching
Allergen detection
ETA estimation
Multilingual support

Demo Video Link:- https://drive.google.com/file/d/18nwwLJi_PEN2dOOizvpEYJGbjsT9nVDO/view?usp=drive_link

Author:
Tushar Kakad
