from fastapi import FastAPI
from .database import engine
from. import models
from .routers import user,auth,plan,sales_track


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


models.Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(plan.router)
app.include_router(sales_track.router)


