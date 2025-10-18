from pydantic import BaseModel
from typing import Any, Optional

class Cookie(BaseModel):
    domain: str
    expirationDate: float
    hostOnly: bool
    httpOnly: bool
    name: str
    path: str
    sameSite: Optional[str]
    secure: bool
    session: bool
    storeId: Optional[Any]
    value: str