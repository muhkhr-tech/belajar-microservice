from sqlalchemy.orm import Session

from . import models, schemas


def login_user(db: Session, form: schemas.UserSignIn):
    user = db.query(models.User).filter(models.User.email == form.email).first()

    if user and user.password == form.password:
        return user
        
    return False