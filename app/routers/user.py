from fastapi import FastAPI,Depends , APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from.. import schemas
from.. import models

router = APIRouter()

@router.post("/register",response_model=schemas.UserResponse)
def Create_user(user:schemas.UserCreate,db:Session =Depends(get_db)):
    new_user =  models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
