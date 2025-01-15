from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    created_at: datetime.time
    username: str
    password: str


class ReadUsers(BaseModel):
    id: int
    created_at: datetime.time
    username: str
    password: str
    class Config:
        from_attributes = True


class Interests(BaseModel):
    id: int
    created_at: datetime.time
    Activities: str
    Groups: str
    Languages: str
    Budget_range: str
    Distance_range: str


class ReadInterests(BaseModel):
    id: int
    created_at: datetime.time
    Activities: str
    Groups: str
    Languages: str
    Budget_range: str
    Distance_range: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: str
    created_at: str
    username: str
    password: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    created_at: str
    username: str
    password: str

    class Config:
        from_attributes = True



class PostInterests(BaseModel):
    id: str
    created_at: str
    Activities: str
    Groups: str
    Languages: str
    Budget_range: str
    Distance_range: str

    class Config:
        from_attributes = True



class PutInterestsId(BaseModel):
    id: str
    created_at: str
    Activities: str
    Groups: str
    Languages: str
    Budget_range: str
    Distance_range: str

    class Config:
        from_attributes = True

