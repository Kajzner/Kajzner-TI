import os
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Person, PersonCreate
from db_config import get_db_session, ORMBaseModel, db_engine
from encoders import to_dict

# Tworzenie tabel przy starcie (jeśli nie istnieją)
ORMBaseModel.metadata.create_all(bind=db_engine)

# Inicjalizacja aplikacji FastAPI
app = FastAPI()

# Definicja routera (endpointy pod /person/)
router = APIRouter()

@router.post("/person/")
def create_person(person: PersonCreate, db: Session = Depends(get_db_session)):
    db_person = Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return to_dict(db_person)

@router.get("/person/")
def read_all_persons(db: Session = Depends(get_db_session)):
    persons = db.query(Person).all()
    return [to_dict(p) for p in persons]

@router.get("/person/{person_id}")
def read_person(person_id: int, db: Session = Depends(get_db_session)):
    person = db.query(Person).filter(Person.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return to_dict(person)

@router.put("/person/{person_id}")
def update_person(person_id: int, updated: PersonCreate, db: Session = Depends(get_db_session)):
    person = db.query(Person).filter(Person.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    for key, value in updated.dict().items():
        setattr(person, key, value)
    db.commit()
    return to_dict(person)

@router.delete("/person/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db_session)):
    person = db.query(Person).filter(Person.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(person)
    db.commit()
    return {"message": f"Deleted person with ID {person_id}"}

# Rejestracja routera
app.include_router(router)
