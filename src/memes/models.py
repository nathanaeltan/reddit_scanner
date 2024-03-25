from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.database import Base

MemeAuthor = Table('meme_author', Base.metadata,
                    Column('meme_id', String, ForeignKey('memes.id')),
                    Column('author_id', String, ForeignKey('authors.id'))
                    )


class Meme(Base):
    __tablename__ = 'memes'
    id = Column(String, primary_key=True, autoincrement=False, index=True)
    title = Column(String)
    url = Column(String)
    score = Column(Integer)
    created_at = Column(DateTime)

    authors = relationship('Author', secondary=MemeAuthor, back_populates='memes')


class Author(Base):
    __tablename__ = 'authors'
    id = Column(String, primary_key=True, autoincrement=False, index=True)
    name = Column(String)

    memes = relationship('Meme', secondary=MemeAuthor, back_populates='authors')
