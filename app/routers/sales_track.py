from fastapi import FastAPI,Depends , APIRouter , HTTPException,status
from ..database import get_db
from sqlalchemy.orm import Session
from.. import schemas
from.. import models


router = APIRouter()

@router.post("/sales",response_model=schemas.sales_trackResponse)
def create_sales(sales:schemas.Sales_track,db:Session=Depends(get_db)):
    new_sales = models.Sales_Tracker(**sales.dict())
    db.add(new_sales)
    db.commit()
    db.refresh(new_sales)
    return new_sales

@router.get("/sales/{id}")
def get_sales(id:int,db:Session=Depends(get_db)):
    sales = db.query(models.Sales_Tracker).filter(models.Sales_Tracker.id ==id).first()
    if not sales:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id no .{id} not found")
    return sales
