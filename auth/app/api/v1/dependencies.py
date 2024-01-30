#type:ignore

from fastapi import Header, HTTPException, status
from typing import Annotated

from ... import utils

async def get_token_header(token: Annotated[str, Header()]):
    if token:
        if utils.is_token_valid(token):
            return True

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token tidak dikenali",
        headers={"WWW-Authenticate": "Bearer"}
    )