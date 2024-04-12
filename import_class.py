from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Дозволяємо запити з усіх джерел, дозволяємо усі методи (GET, POST, PUT, DELETE і т.д.), дозволяємо усі заголовки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],