import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) #Create de user colum, primary key set to make unique the ID
    username = Column(String(250), nullable=False) #nullable false stands for accepting null data or not
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))#Declares that FK is gonna relate to user PK
    user = relationship(User)#FK relates to user PK

    
class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    autor_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    autor_user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(User)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
