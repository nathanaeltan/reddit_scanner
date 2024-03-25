from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

from src.database import create_tables
import src.crawler.router as crawler_router
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()
app = FastAPI()
base_router = APIRouter(prefix="/api")
create_tables()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
base_router.include_router(crawler_router.router)
app.include_router(base_router)