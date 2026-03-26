import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API key is not in .env file")

app = FastAPI()
memory = {}

class Message(BaseModel):
    session_id : str
    customer_name : str
    message : str

name = "Parkash"
memebership = "VIP"

def build_system_prompt(customer_name, membership):
    return f""" 
    You are Muzo, a restaurant assistant for Pizza Hut. 
    Your goal is to answer questions of customers related to Pizza Hut,
    menu, reservations, and timing. Always be polite, calm, and friendly,
    and keep responses clear and concise. If any unrelated question is asked,
    don't answer them and make them get to conversation.
    Always respond in this JSON format:
    { 
        "category": "Menu or Reservation or Complaint or other", 
        "answer": "your answer here", "follow_up": 
        "a follow-up question if needed." 
    }
    Do not add any extra text outside the JSON.
    Examples: 
    User: Do you have spicy pizza? 
    Response: { 
        "category": "Menu",
        "answer": "Yes, we have spicy pizza with fresh tomatoes and chicken!",
        "follow_up": "Would you like medium or extra spicy?" 
    }
    User: I want to book a table for 8. 
    Response: { 
        "category": "Reservation",
        "answer": "I can help with that!",
        "follow_up": "What date and time works for you?" 
    }
    User: Your pizza was 20 minutes late.
    Response:{ 
        "category": "Complaint",
        "answer": "Thanks for coming to Pizza Hut. We're very sorry to hear that. It's Resolution Day, and it's a bit crowded. We will try to make it better; you don't have to face that problem again.",
        "follow_up": "Is there anything else we can help you with?"
    }
    User: What's the capital of Paris?
    Response:{ 
        "category": "Other", 
        "answer": "Sorry, I cannot answer that. I can help you with questions related to our restaurant, or Menu or reservation ", 
        "follow_up": "Do you want to ask anything related to our restaurant or our Menu or reservation?"
    }
"""
def ask_ai(chat_history):
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "llama-3.3-70b-versatile",
                "temperature": 0.3,
                "max_tokens": 500,
                "message": [
                    {"role": "system", "content": f"{build_system_prompt(name, memebership)}"},

                    *chat_history
                ]
            },
            timeout=10
        )
        raw = response.json()["choices"][0]["message"]["content"]
        return json.loads(raw)
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "Connection error. Please check your network"
    except requests.exceptions.HTTPError as e:
        return f"API Error: {e.response.status_code}"
    except Exception as e:
        return f"Something went wrong: {str(e)}"


@app.post("/restaurant-assistant")
def restaurant_chat(messages: Message):
    if not messages.session_id:
        return {"error" : "Session ID is missing"}
    if not messages.message:
        return {"error" : "Please type a message before sending"}
    
    session_id = messages.session_id
    user_message = messages.message

    if session_id not in memory:
        memory[session_id] = [] 

    memory[session_id].append({"role":"user", "content": user_message})
    ai_reply = ask_ai(memory[session_id])

    memory[session_id].append({"role":"assistant", "content": ai_reply})
    return {"reply": ai_reply}

