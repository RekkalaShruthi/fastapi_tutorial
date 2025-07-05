from fastapi import APIRouter, Depends, status
from .. import schemas, database, OAuth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def read_all(db: Session = Depends(database.get_db),
             get_current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.show_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.creating(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.deleting(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.BlogBase, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.updating(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def read(id: int, db: Session = Depends(database.get_db),
         current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.reading(id, db)
