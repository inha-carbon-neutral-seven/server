import openai

from fastapi import APIRouter

from ..models.generate import Question
from ..setting import Settings


generate_router = APIRouter()


@generate_router.post("/generate")
async def generate_message(question: Question):
    """
    모델 서버에 대답을 요청하여 클라이언트에게 전달합니다.
    또한, 대화 기록을 서버에 저장합니다.
    """
    openai.api_key = "empty"
    openai.api_base = Settings().llm_server_URL
    messages = [
        {
            "role": "system",
            "content": "당신은 AI 챗봇이며, 사용자에게 도움이 되는 유익한 내용을 제공해야 합니다."
            + " 답변은 길고 자세하게 친절한 설명을 덧붙여 작성하세요.",
        },
    ]
    message = question
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model=Settings().llm_server_ChatCompletion, messages=messages
    )

    chat_message = response["choices"][0]["message"]["content"]
    return {"message": chat_message}