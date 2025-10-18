from typing import List
from app.models.cookie import Cookie

def transform_cookies(cookies: List[Cookie]) -> List[dict]:
    return [
        {
            "domain": cookie.domain,
            "expires": cookie.expirationDate,
            "httpOnly": cookie.httpOnly,
            "name": cookie.name,
            "path": cookie.path,
            "priority": "Medium",
            "sameParty": False,
            "sameSite": cookie.sameSite.capitalize() if cookie.sameSite else "None",
            "secure": cookie.secure,
            "session": cookie.session,
            "size": len(cookie.name + cookie.value),
            "sourcePort": 443,
            "sourceScheme": "Secure",
            "value": cookie.value
        }
        for cookie in cookies if cookie.domain == "www.daft.ie"
    ]