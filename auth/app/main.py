from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from jose import jwt
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import os

from . import crud, models, schemas
from .database import SessionLocal, engine

load_dotenv()

app = FastAPI()

origins = [
    "http://0.0.0.0:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login")
def login(form: schemas.UserSignIn, db: Session = Depends(get_db)):

    user = crud.login_user(db, form)

    if user:
        token = jwt.encode({'sub': user.email}, os.getenv('SECRET_AUTH'), algorithm='HS256')

        return {
            'status': 'success',
            'code': 200,
            'message': 'Berhasil login!',
            'data': {
                'access_token': token
            }
        }

    else:
        return {
            'status': 'failed',
            'code': 404,
            'message': 'Gagal login!',
            'data': None
        }