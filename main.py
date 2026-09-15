from fastapi import FastAPI

from routers.user import router as user_router
from routers.category import router as category_router
from routers.vision_item import router as vision_item_router

from database import Base, engine

from models.user import User
from models.category import Category
from models.vision_item import VisionItem


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="DreamBoard API"
)


app.include_router(user_router)
app.include_router(category_router)
app.include_router(vision_item_router)