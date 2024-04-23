from fastapi import FastAPI
from src.v1.gateways.http import AppRoute
from config.database import init_db

app = FastAPI()

# register http route
app.include_router(AppRoute)

# init db model
init_db()

# grpc
# tbd

# run fast api
# uvicorn main:app --reload