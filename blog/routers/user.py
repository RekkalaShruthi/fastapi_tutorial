from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', response_model=schemas.UserBase)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.creating(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def read(id: int, db: Session = Depends(database.get_db)):
    return user.reading(id, db)
