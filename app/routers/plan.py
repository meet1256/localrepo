from fastapi import FastAPI ,APIRouter,HTTPException,status
from ..schemas import Plans
router = APIRouter()


plans = [
    Plans(id=1,name="Free",price=0.0,features=["track 2 products", "automated sales notifications through discord","Fulfillment Unlimeted orders"], duration="Monthly"),
    Plans(id=2,name="Standard",price=399.0,features=["track 25 products", "automated sales notifications through discord","Fulfillment Unlimeted orders"], duration="Monthly"),
    Plans(id=3,name="Free",price=699.0,features=["track 50 products", "automated sales notifications through discord","list of Top fulfillment","Fulfillment Unlimeted orders"], duration="Monthly"),
    Plans(id=4,name="Free",price=999.0,features=["track 100 products"," automated sales notifications through discord","list of Top fulfillment","Fulfillment Unlimeted orders"], duration="Monthly")
]

@router.get("/plans")
def get_all_plans():
    return plans

@router.get("/plans/{plan_id}",response_model=Plans)
def get_plann_by_id(plan_id:int):
    for plan in plans:
        if plan.id == plan_id:
            return plan
        if plan not in plans:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="plan not found")

