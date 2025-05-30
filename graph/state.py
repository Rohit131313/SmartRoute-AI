from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class GraphState(BaseModel):
    file_type: str
    file_content: str
    intent: str
