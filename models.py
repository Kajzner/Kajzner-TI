from sqlalchemy import Column, Integer, String, Float
from db_config import ORMBaseModel
from pydantic import BaseModel

# TODO Wzorując się na poniższych przykładach, zdefiniuj odpowienie modele w swojej aplikacji.

class Person(ORMBaseModel):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    person_type_id = Column(Integer, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)


class PersonCreate(BaseModel):
    first_name: str
    last_name: str
    person_type_id: int
    age: int
    latitude: float | None = None
    longitude: float | None = None


class PositionUpdate(BaseModel):
    latitude: float
    longitude: float

