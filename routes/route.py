from fastapi import APIRouter,Depends, HTTPException
from config.db import get_db
from models.person import Persona
from schemas.person import PersonCreate
from sqlalchemy.orm import Session

persons = APIRouter()

@persons.get("")
def get_persons(db: Session = Depends(get_db)):
  persons = db.query(Persona).all()
  return persons

@persons.post("")
def create_person(person: PersonCreate,db: Session = Depends(get_db)):
  db_person = Persona(
    nombre = person.nombre,
    edad = person.edad,
    trabajo = person.trabajo
  )
  db.add(db_person)
  db.commit()
  db.refresh(db_person)
  return db_person

@persons.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
  person = db.query(Persona).filter(Persona.id == id).first()
  if person is None:
    raise HTTPException(status_code=404, detail = "Not found")
  return person