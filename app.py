from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.route import persons

app = FastAPI()
app.include_router(persons, prefix="/persons")

origins = [
  "http://localhost:3000"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_methods=["GET", "POST"]
)

# uvicorn app:app --reload

# API
# getAll,
# getyId,
# post,
