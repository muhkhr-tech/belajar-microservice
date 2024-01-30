#type:ignore

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta

from . import crud, schemas, utils
from .api.v1 import routes as api_v1_routes
from .database import SessionLocal

load_dotenv()

app = FastAPI()

origins = [
    "http://0.0.0.0:3000",
]

ACCESS_TOKEN_EXPIRE_MINUTES=60

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_routes.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login", tags=["User Auth"])
def login(form: schemas.UserSignIn, db: Session = Depends(get_db)) -> schemas.Token:

    user = utils.authenticate_user(db, form)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username atau password salah",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data={'sub': user.email}, expires_delta=access_token_expires
    )

    return schemas.Token(access_token=access_token, token_type="Bearer")

@app.post("/register", tags=["User Auth"])
def register(form: schemas.UserRegister, db: Session = Depends(get_db)):

    user = crud.register_user(db, form)

    return {"message": "Berhasil melakukan registrasi"}