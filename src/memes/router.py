from fastapi import APIRouter
from dotenv import load_dotenv
from starlette import status
from src.database import db_dependency
from src.memes.services import MemeServices
from src.memes.utils import get_memes, has_cached_memes

load_dotenv()

router = APIRouter(
    prefix='/memes',
    tags=['memes']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def get_reddit_memes(db: db_dependency):
    meme_service = MemeServices(db)
    if has_cached_memes():
        meme_list = meme_service.find_most_recent_memes()
        if len(meme_list) == 20:
            return meme_list
    memes = await get_memes()
    memes = meme_service.save_memes(memes)

    return memes


@router.get("/", status_code=status.HTTP_200_OK)
async def get_memes(db: db_dependency):
    meme_service = MemeServices(db).get_all_memes()
    return meme_service
