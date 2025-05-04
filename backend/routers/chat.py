from fastapi import APIRouter
from services.handlers import handle_compatibility_check, handle_install, handle_product_info, handle_troubleshooting, handle_order_status, handle_off_topic, handle_small_talk, handle_unknown
from models.schemas import ChatRequest, ChatResponse
from services.intent_classifier import classify_intent

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_handler(req: ChatRequest):
    intent = await classify_intent(req.message)

    if intent == "compatibility_check":
        message = await handle_compatibility_check(req.message)
    elif intent == "installation_help":
        message = await handle_install(req.message)
    elif intent == "product_info":
        message = await handle_product_info(req.message)
    elif intent == "troubleshooting":
        message = await handle_troubleshooting(req.message)
    elif intent == "order_status":
        message = await handle_order_status(req.message)
    elif intent == "off_topic":
        message = await handle_off_topic(req.message)
    elif intent == "small_talk":
        message = await handle_small_talk(req.message)
    else:
        message = await handle_unknown(req.message)

    return ChatResponse(
        reply=message,
        metadata={}
    )