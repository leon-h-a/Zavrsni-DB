from sqlalchemy import Column, Integer, String
from models import Base


class Microcontroller(Base):
    __tablename__ = 'microcontroller'
    id = Column(Integer, primary_key=True)
    name_on_initialisation = Column(String)
    human_readable_name = Column(String)

    def __repr__(self):
        return "<User(name_on_initialisation='%s', fullname='%s')>" %\
               (self.name_on_initialisation, self.human_readable_name)
