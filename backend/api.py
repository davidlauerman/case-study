"""
Input Processing:
    Recieve input and classify into the following
    product_info, installation_help, troubleshooting, compatibility_check, order_status, off_topic
RAG:
    Retrieve context to append to Deepseek call
    Langchain, setup a Pinecone vector db for specific info
Deepseek query
    Structure response for frontend display
    System:
        You are a helpful assistant on the PartSelect website. You only answer questions about refrigerator and dishwasher parts. You provide accurate, clear information based on documentation provided.
    Context:
        {{retrieved_docs}}
    User:
        {{user_query}}
    Rules:
        - Recommend only compatible parts for the user's model.
        - Never speculate about unsupported products.
        - If unsure, ask for a model number or part ID.
        - Format part suggestions as JSON metadata for UI rendering.
Further ideas to keep in mind:
    New product categories (e.g., ovens, washers)
    Personalization layer (if logged in)
"""

from fastapi import FastAPI
from routers import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")