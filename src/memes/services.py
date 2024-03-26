from src.memes.models import Author, Meme
from datetime import datetime, timedelta
from typing import List

from src.memes.schemas import SaveMemeRequest


class MemeServices:
    def __init__(self, db):
        self.db = db

    def find_most_recent_memes(self):
        db = self.db
        last_24_hours = datetime.utcnow() - timedelta(hours=24)
        memes = db.query(Meme, Author).filter(Meme.created_at >= last_24_hours).order_by(Meme.score.desc()).join(Author, Meme.author_id == Author.id).limit(20).all()
        memes_dict_list = []
        for meme, author in memes:
            meme_dict = {
                'id': meme.id,
                'title': meme.title,
                'score': meme.score,
                'url': meme.url,
                'created_utc': meme.created_at,
                'author_name': author.name,
                'author_id': author.id
            }
            memes_dict_list.append(meme_dict)
        return memes_dict_list

    def save_memes(self, meme_list: List[SaveMemeRequest]):
        db = self.db
        for meme_entry in meme_list:
            utc_datetime = datetime.utcfromtimestamp(meme_entry['created_utc'])
            existing_meme = db.query(Meme).filter(Meme.id == meme_entry['id']).first()
            if existing_meme:
                continue
            meme = Meme(id=meme_entry['id'], title=meme_entry['title'], url=meme_entry['url'],
                        score=meme_entry['score'],
                        created_at=utc_datetime, author_id=meme_entry['author_id'])
            author = db.query(Author).filter(Author.id == meme_entry['author_id']).first()
            if not author:
                author = Author(name=meme_entry['author'], id=meme_entry['author_id'])

            meme.authors.append(author)
            db.add(meme)
            db.commit()
        return meme_list

    def get_all_memes(self):
        db = self.db
        memes = db.query(Meme, Author).join(Author, Meme.author_id == Author.id).all()
        memes_dict_list = []
        for meme, author in memes:
            meme_dict = {
                'id': meme.id,
                'title': meme.title,
                'score': meme.score,
                'url': meme.url,
                'created_utc': meme.created_at,
                'author_name': author.name,
                'author_id': author.id
            }
            memes_dict_list.append(meme_dict)
        return memes_dict_list
