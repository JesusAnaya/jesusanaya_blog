# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime,
)
from .meta import Base


class User(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    path = Column(Unicode(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __json__(self, request=None):
        return {
            'id': self.id,
            'path': self.first_name,
            'created_at': self.full_name,
        }

    def __str__(self):
        return self.path
