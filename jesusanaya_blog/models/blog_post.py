# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime,
    ForeignKey,
    UnicodeText,
    Enum,
)
from .meta import Base


class BlogPost(Base):
    __tablename__ = 'blog_post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    title = Column(Unicode(255), nullable=False)
    slug = Column(Unicode(280), nullable=False)
    body = Column(UnicodeText, nullable=True)
    status = Column(Enum('published', 'draft', name='blog_post_statuses'),
        nullable=False, default='draft')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    author = relationship("User", backref="blog_posts")

    def __json__(self, request=None):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'body': self.body,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __str__(self):
        return self.title
