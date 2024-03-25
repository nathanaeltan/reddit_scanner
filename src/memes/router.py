from fastapi import APIRouter, Depends, HTTPException
import praw
from dotenv import load_dotenv

from src.memes.utils import get_memes

load_dotenv()

router = APIRouter(
    prefix='/memes',
    tags=['memes']
)

@router.get("/")
async def get_reddit_memes():
    memes = get_memes()
    return memes