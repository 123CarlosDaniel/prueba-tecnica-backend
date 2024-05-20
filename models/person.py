from config.db import Base, engine
from sqlalchemy import Column, Integer, VARCHAR

class Persona(Base):
  __tablename__ = "Personas"
  id = Column(Integer,primary_key=True, autoincrement=True)
  nombre = Column(VARCHAR(80), nullable=False)
  edad = Column(Integer, nullable=False)
  trabajo = Column(VARCHAR(80))

Base.metadata.create_all(bind=engine)
