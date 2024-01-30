#type:ignore
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models, utils


def register_user(db: Session, form: dict):
    user = db.query(models.User).filter(models.User.email == form.email).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User dengan email {form.email} sudah digunakan"
        )

    new_user = models.User()
    new_user.name = form.name
    new_user.email = form.email
    new_user.password = utils.get_password_hashed(form.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user