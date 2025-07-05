from sqlalchemy.orm import Session
from .. import schemas, database, models, tokens
from fastapi import APIRouter, Depends, HTTPException, status
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix='/login',
    tags=['authentication']
)


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Inncorrect Password")

    access_token = tokens.create_access_token(
        data={"sub": user.email}  # sending the data
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
