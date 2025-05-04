from dotenv import load_dotenv
import os
from typing import Literal
import cohere
from cohere import ClassifyExample

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

Intent = Literal[
    "product_info", "installation_help", "troubleshooting", 
    "compatibility_check", "order_status", "off_topic", "small_talk"
]

co = cohere.Client("dh2DjHysTfoxViTn8w0LMEZJOWtmBT8IDtKugCkT")

EXAMPLES = [
    ClassifyExample(text="Is part number PS11752778 compatible with Whirlpool WDT780SAEM1?", label="compatibility_check"),
    ClassifyExample(text="Does PS11750510 work with my fridge model WRX735SDBM00?", label="compatibility_check"),
    ClassifyExample(text="Tell me more about part number PS1234567", label="product_info"),
    ClassifyExample(text="What is the best fridge?", label="product_info"),
    ClassifyExample(text="Tell me more about my fridge?", label="product_info"),
    ClassifyExample(text="What type of fridge is my H459498448 fridge?", label="product_info"),
    ClassifyExample(text="How can I install part number PS1175998?", label="installation_help"),
    ClassifyExample(text="How do I attach this fridge to the wall", label="installation_help"),
    ClassifyExample(text="How do I install my new dishwasher model?", label="installation_help"),
    ClassifyExample(text="How do I put this dishwasher in", label="installation_help"),
    ClassifyExample(text="The ice maker on my Whirlpool fridge isn't working", label="troubleshooting"),
    ClassifyExample(text="My dishwasher won't start", label="troubleshooting"),
    ClassifyExample(text="My dishwasher is broken", label="troubleshooting"),
    ClassifyExample(text="My refrigerator won't work, it is not turning on", label="troubleshooting"),
    ClassifyExample(text="Where is my order?", label="order_status"),
    ClassifyExample(text="When will my fridge arrive?", label="order_status"),
    ClassifyExample(text="Hi there!", label="small_talk"),
    ClassifyExample(text="Thanks for the help!", label="small_talk"),
    ClassifyExample(text="How do I install my new stove?", label="off_topic"),
    ClassifyExample(text="akjshdfkjahsdf", label="off_topic"),
    ClassifyExample(text="anything else", label="off_topic"),
    ClassifyExample(text="Do I have a microwave?", label="off_topic"),
    ClassifyExample(text="How do I fix my stove?", label="off_topic"),
    ClassifyExample(text="How do I install this PS11752778 sink?", label="off_topic"),
]

async def classify_intent(message: str) -> Intent:
    response = co.classify(
        model="df7181da-9d17-4e01-99a5-957c63f4c5f6-ft",
        inputs=[message],
        examples=EXAMPLES,
    )
    prediction = response.classifications[0].predictions[0]
    return prediction if prediction in Intent.__args__ else "off_topic"

