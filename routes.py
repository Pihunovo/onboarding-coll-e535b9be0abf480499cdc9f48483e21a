from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/interests/')
async def get_interests(db: Session = Depends(get_db)):
    try:
        return await service.get_interests(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/interests/id')
async def get_interests_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_interests_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/interests/')
async def post_interests(raw_data: schemas.PostInterests, db: Session = Depends(get_db)):
    try:
        return await service.post_interests(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/interests/id/')
async def put_interests_id(raw_data: schemas.PutInterestsId, db: Session = Depends(get_db)):
    try:
        return await service.put_interests_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/interests/id')
async def delete_interests_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_interests_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

