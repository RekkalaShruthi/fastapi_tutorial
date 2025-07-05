from .. import models, hashing, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def creating(request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.email == request.email)
    if user.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"email {request.email} exist, please try another")

    new_user = models.User(
        name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def reading(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with id {id} is not available')
    return user
