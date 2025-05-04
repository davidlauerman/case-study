from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str]

class ChatResponse(BaseModel):
    reply: str
    metadata: Optional[dict]

class PartDetail(BaseModel):
    part_number: str
    name: str
    price: float
    description: str
    image_url: str
    in_stock: bool

class CompatibilityResponse(BaseModel):
    part: str
    model: str
    compatible: bool

class InstallGuide(BaseModel):
    part_number: str
    steps: List[str]

class TroubleshootRequest(BaseModel):
    appliance_type: str
    symptom: str

class TroubleshootResponse(BaseModel):
    appliance: str
    issue: str
    suggestions: List[str]