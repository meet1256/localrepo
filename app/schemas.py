from fastapi import FastAPI 
from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import List,Optional




class UserCreate(BaseModel):
    firstname :str
    lastname : str
    phone_number :str
    email_id : EmailStr
    hashed_password :str

class UserResponse(BaseModel):
    id:int
    created_at : datetime

    class config:
        from_attribute : True
        
class Plans(BaseModel):
    id:int
    name:str
    price:float
    features:List[str]
    duration: Optional[str]="Monthly"


class Sales_track(BaseModel):
    url:str
    currency:str
    notification:bool
class sales_trackResponse(BaseModel):
    id:int
    class config:
        from_attrinute :True




