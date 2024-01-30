from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import ExpiredSignatureError
from datetime import timedelta, timezone, datetime

import os


def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=1)

    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))

    return encode_jwt

def is_token_valid(token: str):

    try:
        decode_jwt = jwt.decode(token, os.getenv('SECRET_KEY'), os.getenv('ALGORITHM'))
        return decode_jwt

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token sudah tidak aktif",
            headers={"WWW-Authenticate": "Bearer"}
        )

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token tidak valid",
            headers={"WWW-Authenticate": "Bearer"}
        )

