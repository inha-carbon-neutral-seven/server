from fastapi import APIRouter


ping_router = APIRouter()


@ping_router.get("/ping")
async def ping():
    """
    웹 서버와 모델 서버의 상태를 확인합니다.
    모델 서버가 꺼져 있으면 false를 return 합니다.
    """
    return {"pong": True}