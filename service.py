from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_users(db: Session):

    Users_all = db.query(models.Users).order_by(models.Users.id).all()
    res = {
        'Users_all': Users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    Users_one = db.query(models.Users).filter(models.Users.id == 'id').first()
    res = {
        'Users_one': Users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    username:str = raw_data.username
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'created_at': created_at, 'username': username, 'password': password}
    new_Users = models.Users(**record_to_be_added)
    db.add(new_Users)
    db.commit()
    db.refresh(new_Users)
    Users_inserted_record = new_Users
    res = {
        'Users_inserted_record': Users_inserted_record,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    username:str = raw_data.username
    password:str = raw_data.password


    Users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'username': username, 'password': password}.items():
          setattr(Users_edited_record, key, value)
    db.commit()
    db.refresh(Users_edited_record)
    Users_edited_record = Users_edited_record

    res = {
        'Users_edited_record': Users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    Users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Users_deleted = record_to_delete
    res = {
        'Users_deleted': Users_deleted,
    }
    return res

async def get_interests(db: Session):

    Interests_all = db.query(models.Interests).order_by(models.Interests.id).all()
    res = {
        'Interests_all': Interests_all,
    }
    return res

async def get_interests_id(db: Session, id: int):

    Interests_one = db.query(models.Interests).filter(models.Interests.id == 'id').first()
    res = {
        'Interests_one': Interests_one,
    }
    return res

async def post_interests(db: Session, raw_data: schemas.PostInterests):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    Activities:str = raw_data.Activities
    Groups:str = raw_data.Groups
    Languages:str = raw_data.Languages
    Budget_range:str = raw_data.Budget_range
    Distance_range:str = raw_data.Distance_range


    record_to_be_added = {'id': id, 'created_at': created_at, 'Activities': Activities, 'Groups': Groups, 'Languages': Languages, 'Budget_range': Budget_range, 'Distance_range': Distance_range}
    new_Interests = models.Interests(**record_to_be_added)
    db.add(new_Interests)
    db.commit()
    db.refresh(new_Interests)
    Interests_inserted_record = new_Interests
    res = {
        'Interests_inserted_record': Interests_inserted_record,
    }
    return res

async def put_interests_id(db: Session, raw_data: schemas.PutInterestsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    Activities:str = raw_data.Activities
    Groups:str = raw_data.Groups
    Languages:str = raw_data.Languages
    Budget_range:str = raw_data.Budget_range
    Distance_range:str = raw_data.Distance_range


    Interests_edited_record = db.query(models.Interests).filter(models.Interests.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'Activities': Activities, 'Groups': Groups, 'Languages': Languages, 'Budget_range': Budget_range, 'Distance_range': Distance_range}.items():
          setattr(Interests_edited_record, key, value)
    db.commit()
    db.refresh(Interests_edited_record)
    Interests_edited_record = Interests_edited_record

    res = {
        'Interests_edited_record': Interests_edited_record,
    }
    return res

async def delete_interests_id(db: Session, id: int):

    Interests_deleted = None
    record_to_delete = db.query(models.Interests).filter(models.Interests.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Interests_deleted = record_to_delete
    res = {
        'Interests_deleted': Interests_deleted,
    }
    return res

