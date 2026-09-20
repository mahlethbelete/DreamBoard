from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routers.auth import router as auth_router
from routers.user import router as user_router
from routers.category import router as category_router
from routers.vision_item import router as vision_item_router
from routers.upload import router as upload_router
from routers.ai import router as ai_router
from routers.images import router as images_router

from database import Base, engine

from models.user import User
from models.category import Category
from models.vision_item import VisionItem


import os

os.makedirs("uploads", exist_ok=True)

app = FastAPI(title="DreamBoard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_origin_regex=r"https://dream-board-liora-frontend.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(vision_item_router)
app.include_router(upload_router)
app.include_router(ai_router)
app.include_router(images_router)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
