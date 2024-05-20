from pydantic import BaseModel

class PersonBase(BaseModel):
  nombre: str
  edad: int
  trabajo: str

class Person(PersonBase):
  id: int
  
class PersonCreate(PersonBase):
  pass