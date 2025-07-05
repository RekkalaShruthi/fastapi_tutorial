from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def show_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def creating(request: schemas.Blog, db: Session):
    user = db.query(models.User).filter(models.User.id == request.user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with user id {request.user_id} does not exist')
    new_blog = models.Blog(
        title=request.title, body=request.body, user_id=request.user_id)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def deleting(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with id {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def updating(id: int, request: schemas.BlogBase, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with id {id} not found')

    blog.update(request.dict())
    db.commit()
    return 'updated'


def reading(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'blog with id {id} is not available'}

    return blog
