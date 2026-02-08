# Discord-RAG-FAQ-Chatbot
A backend system that connects a Discord chatbot with a Retrieval-Augmented Generation (RAG) agent powered by Google Gemini.  
The backend is responsible for API design, LLM integration, logging, observability, and containerized deployment.

This project focuses on **backend architecture and operational excellence**, rather than frontend UI or model training.

# Architecture Overview
```
Discord Bot
-> HTTP (POST /api/rag-query)
-> FastAPI Backend (Docker)
-> Prompt-based RAG logic
-> Google Gemini API
```

# Key Responsibilities of the Backend
- Receive user questions from a Discord bot
- Process Python-related queries using a Gemini-powered RAG agent
- Return structured responses
- Provide logging and observability
- Support containerized deployment via Docker

# Running Locally (Without Docker)
Note: you need to create a Discord bot first in [Discord Developer Portal](https://discord.com/developers/applications).
### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Fill Keys in `.env`
```
GEMINI_API_KEY=your_api_key
DISCORD_TOKEN=your_discord_bot_token
```

### 3. Start Backend Under the Project Folder in Terminal
```
uvicorn app.main:app --reload --env-file .env
```

### 4. Start Discord Bot Under the Project Folder in New Terminal
```
python app/discord_bot.py
```

### 5. Use in Discord
Type the question after `!py` to ask your bot in Discord. <br>
Example:
```
!py What is a Python decorator?
```

# Running with Docker
Note: you may need to download [Docker Desktop](https://www.docker.com/products/docker-desktop/) first.

### 1. Fill Keys in `.env`
```
GEMINI_API_KEY=your_api_key
DISCORD_TOKEN=your_discord_bot_token
```

### 2. Build Image
After running Docker Desktop, open a terminal and navigate to the project folder to type the below command:<br>
```
docker build -t discord-rag-backend .
```

### 3. Run Container
In the same terminal, run: <br>
```
docker run --env-file .env -p 8000:8000 discord-rag-backend
```

### 4. Test API
Keep the last terminal open, and open new terminal under the project folder. Type: 
```
curl -X POST http://localhost:8000/api/rag-query ^
  -H "Content-Type: application/json" ^
  -d "{\"user_id\":\"test\",\"query\":\"What is a Python decorator?\"}"
```
You should get answer.

### 5. Use in Discord
Open new terminal under the project folder and type:
```
python app/discord_bot.py
```

Open Discord and type the question after `!py` to ask your bot in Discord.
