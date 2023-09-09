import os
from fastapi.security.api_key import APIKeyHeader, APIKey
from fastapi import HTTPException, Security
from starlette.status import HTTP_403_FORBIDDEN

UserSession = APIKey
API_KEY = os.getenv("TOKEN_SECRET_KEY")
API_KEY_NAME = "x-iaps-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def validate_token(iaps_api_key: str = Security(api_key_header)):
    if iaps_api_key == API_KEY:
        return iaps_api_key
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Wrong X-iaps-Api-Key.")
