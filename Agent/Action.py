from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class Action(BaseModel):
    name: str = Field(description="Tool or Command Name")
    args: Optional[Dict[str, Any]] = Field(description="Tools or command parameters, composed of parameter name and parameter value")
