from fastapi import APIRouter
from models.topic import Topic
from chat.chat import explain
router = APIRouter()

@router.post("/explain")
def get_explaination(data: Topic):
    return explain(data.topic)