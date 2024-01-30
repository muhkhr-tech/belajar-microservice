from fastapi import Depends, FastAPI, HTTPException, Header
from sqlalchemy.orm import Session
from typing import Annotated
from jose import jwt
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

import uvicorn, os

from . import crud, models, schemas
from .database import SessionLocal, engine

load_dotenv()

app = FastAPI()

origins = [
    "http://0.0.0.0:8000",
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

@app.get("/products/")
def read_products(token: Annotated[str | None, Header()], db: Session = Depends(get_db)):
    
    try:
        jwt.decode(token, os.getenv('SECRET_AUTH'))

        products = crud.get_products(db)
        return {
            'status': 'success',
            'code': 200,
            'message': 'Berhasil mengambil data!',
            'data': products
        }

    except:
        return {
            'status': 'failed',
            'code': 401,
            'message': 'Token salah!',
            'data': None
        }