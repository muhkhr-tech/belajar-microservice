#type:ignore

from fastapi import APIRouter, Request, Depends, HTTPException, status, Header
from typing import Annotated

from .dependencies import get_token_header
from ... import schemas


router = APIRouter(
    prefix='/api',
    tags=['API v1'],
    dependencies=[Depends(get_token_header)]
)

@router.get("/token")
def token(token: Annotated[str, Header()]) -> schemas.Token:
    return schemas.Token(
        access_token=token,
        token_type="Bearer"
    )