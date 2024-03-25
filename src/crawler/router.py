from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix='/crawler',
    tags=['crawler']
)

@router.get("/")
async def get_reddit_memes():
    pass