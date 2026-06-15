from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List

from .models import ChatMessageListItem, ChatMessagePayload, ChatMessage

from api.db import get_session

router = APIRouter()

#/api/chat
@router.get("/")
def chat_health():
    return {"status": "Chat API is healthy"}



#api/chat/recent
#curl http://localhost:8000/api/chat/recent/
@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_recent_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage).order_by(ChatMessage.id.desc()).limit(10)
    messages = session.exec(query).fetchall()
    return messages


#add a message
#curl -X POST http://localhost:8000/api/chat/ -H "Content-Type: application/json" -d "{\"message\": \"Hello, World!\"}"
@router.post("/", response_model=ChatMessageListItem)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump()    
    obj = ChatMessage.model_validate(data)
  
    #read to story in database
    session.add(obj)
    session.commit()
    session.refresh(obj)
  
    return obj
