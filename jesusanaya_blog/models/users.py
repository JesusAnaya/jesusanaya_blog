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
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(255), nullable=True)
    last_name = Column(Unicode(255), nullable=True)
    email = Column(Unicode(255), unique=True, nullable=False)
    phone = Column(Unicode(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __json__(self, request=None):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'full_name': self.full_name,
        }

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
