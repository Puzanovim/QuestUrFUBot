from sqlalchemy import Column, Integer, String

from db import Base


class Team(Base):
    __tablename__ = 'teams_quest'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_face = Column(String, nullable=True)
    link_vk = Column(String, nullable=True)
    tel_number = Column(String, nullable=True)
    institute = Column(String, nullable=True)


class TeamPoints(Base):
    __tablename__ = 'points_table_quest'

    user_id = Column(Integer, primary_key=True)
    current_question = Column(Integer, default=0)
    result = Column(Integer, default=0)




