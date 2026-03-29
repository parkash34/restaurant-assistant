# Pizza Hut Restaurant Assistant API

A conversational AI assistant for Pizza Hut built with FastAPI and Groq AI.
The assistant uses advanced prompt engineering techniques to provide
structured, consistent, and context-aware responses to customer queries.

## Features

- Structured JSON responses with category, answer, and follow-up
- Dynamic context injection — today's date, specials, and available tables
- Multi-session conversation memory — each customer has a separate chat history
- Few-shot prompting for consistent response patterns
- Customer personalization — assistant knows the customer's name
- Input validation and comprehensive error handling
- Categories — Menu, Reservation, Complaint, and Other

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend web framework |
| Groq API | AI language model provider |
| LLaMA 3.3 70B | AI model |
| Pydantic | Data validation |
| python-dotenv | Environment variable management |

## Project Structure
```
week5-project/
│
├── .venv/               
├── main.py            
├── .env               
└── requirements.txt   
```

## Setup

1. Clone the repository
```
git clone https://github.com/yourusername/pizza-hut-assistant
```

2. Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key
```
API_KEY=your_groq_api_key_here
```

5. Run the server
```
uvicorn main:app --reload
```

## API Endpoint

### POST /chat

**Request:**
```json
{
    "session_id": "user_1",
    "customer_name": "Ahmed",
    "message": "Do you have a family deal?"
}
```

**Response:**
```json
{
    "category": "Menu",
    "answer": "Yes, we have a family deal!",
    "follow_up": "Would you like to know more details?"
}
```

## Prompt Engineering Techniques Used

- **System prompts** — 5 component professional prompt design
- **Few-shot prompting** — examples for each response category
- **Structured outputs** — forced JSON format responses
- **Dynamic prompts** — real time data injection
- **Role based prompting** — system, user and assistant roles

## Environment Variables
```
API_KEY=your_groq_api_key_here
```

## Notes

- Never commit your `.env` file to GitHub
- The assistant only answers Pizza Hut-related questions
- Each session maintains its own conversation history
- Conversation history resets when the server restarts


## 👤 Author

**Ohm Parkash** — [LinkedIn](https://www.linkedin.com/in/om-parkash34/) · [GitHub](https://github.com/parkash34)
