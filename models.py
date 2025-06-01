from sqlalchemy import Column, Integer, String, Float
from db_config import ORMBaseModel
from pydantic import BaseModel

class Person(ORMBaseModel):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    person_type_id = Column(Integer, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=True)     # NOWE
    longitude = Column(Float, nullable=True)    # NOWE

class PersonCreate(BaseModel):
    first_name: str
    last_name: str
    person_type_id: int
    age: int

class PositionUpdate(BaseModel):  # NOWE
    latitude: float
    longitude: float
