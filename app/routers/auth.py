from app import oauth2, models
from .. import database
# from .. import utils
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login")
def login_user(user:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    existing_user = db.query(models.User).filter(models.User.email_id == user.username).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    password = db.query(models.User).filter(models.User.hashed_password== user.password).first()

    if not password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid password")
    access_token = oauth2.create_access_token(data={"users_id":existing_user.id})
    return {"access_token": access_token, "token_type": "Bearer"}




