from sqlalchemy.orm import Session
from datetime import timedelta, datetime, timezone
from jose import jwt

import os

from . import models, schemas


def authenticate_user(db: Session, form: schemas.UserSignIn):
    user = db.query(models.User).filter(models.User.email == form.email).first()

    if user and user.password == form.password:
        return user
        
    return False