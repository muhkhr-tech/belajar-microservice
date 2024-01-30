#type:ignore

from fastapi import APIRouter, Request, Depends, HTTPException, status, Header
from typing import Annotated

from ... import utils, schemas


async def auth_middleware(request: Request):
    if 'token' in request.headers:
        if utils.is_token_valid(request.headers['token']):
            return True

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token tidak dikenali",
        headers={"WWW-Authenticate": "Bearer"}
    )

router = APIRouter(
    prefix='/api',
    tags=['API v1'],
    dependencies=[Depends(auth_middleware)]
)

@router.get("/token")
def token(token: Annotated[str, Header()]) -> schemas.Token:
    return schemas.Token(
        access_token=token,
        token_type="Bearer"
    )