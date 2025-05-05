from services.deepseek import query_deepseek


async def handle_compatibility_check(message: str) -> str:
    # extract either with entity recognition, regex, or a follow up question
    # search product database, vector search, or external API to determine compatibility
    # the message returned would then be yes or no, perhaps some extra info- but formulaic
    return "Let me check if that part is compatible with your model..."

async def handle_install(message: str) -> str:
    # similar to compatibility check, but run through deepseek to extract meaningful information
    return query_deepseek(message, "", "installation_help")

async def handle_product_info(message: str) -> str:
    # similar to compatibility check, but run through deepseek to extract meaningful information
    return query_deepseek(message, "", "product_info")

async def handle_troubleshooting(message: str) -> str:
    # run message through LLM + RAG / predefined troubleshooting workflows
    return query_deepseek(message, "","troubleshooting")

async def handle_order_status(message: str) -> str:
    # Link to order status API or service
    return "Can you please provide your order number?"

async def handle_small_talk(message: str) -> str:
    return "What can I assist you with?"

async def handle_off_topic(message: str) -> str:
    return "My speciality is Refrigerator and Dishwasher parts. Can I help you with something related to that?"

async def handle_unknown(message: str) -> str:
    return "I'm not sure how to help with that. Could you rephrase?"
