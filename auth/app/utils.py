#type:ignore

from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import ExpiredSignatureError
from datetime import timedelta, timezone, datetime
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import schemas, models

import os


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hashed(password):
    return pwd_context.hash(password)

def authenticate_user(db: Session, form: schemas.UserSignIn):
    user = db.query(models.User).filter(models.User.email == form.email).first()

    if user and verify_password(form.password, user.password):
        return user
        
    return False

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

