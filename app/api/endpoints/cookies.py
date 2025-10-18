from fastapi import APIRouter
from typing import List
from app.models.cookie import Cookie
from app.services.cookie_service import transform_cookies

router = APIRouter()

@router.post("/transform_cookies")
def transform_cookies_endpoint(cookies: List[Cookie]):
    return {"cookies": transform_cookies(cookies)}