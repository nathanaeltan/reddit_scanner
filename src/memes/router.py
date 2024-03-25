from fastapi import APIRouter
from dotenv import load_dotenv
from starlette import status
from src.database import db_dependency
from src.memes.models import Author, Meme, MemeAuthor
from src.memes.utils import get_memes
from datetime import datetime
load_dotenv()

router = APIRouter(
    prefix='/memes',
    tags=['memes']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def get_reddit_memes(db: db_dependency):
    memes = await get_memes()
    for meme_entry in memes:
        utc_datetime = datetime.utcfromtimestamp(meme_entry['created_utc'])
        existing_meme = db.query(Meme).filter(Meme.id == meme_entry['id']).first()
        if existing_meme:
            continue
        meme = Meme(id=meme_entry['id'], title=meme_entry['title'], url=meme_entry['url'], score=meme_entry['score'],
                    created_at=utc_datetime)
        author = db.query(Author).filter(Author.id == meme_entry['author_id']).first()
        if not author:
            author = Author(name=meme_entry['author'], id=meme_entry['author_id'])

        meme.authors.append(author)
        db.add(meme)
        db.commit()


    return memes
