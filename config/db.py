from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://testuser:password@localhost:3306/testdb"

engine = create_engine(DB_URL, echo=True)

session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

Base = declarative_base()

def get_db():
  db = session()
  try:
    yield db
  finally:
    db.close()