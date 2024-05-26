from fastapi import FastAPI, Request
from routes import pokemon_routes
import data.models as models
from data.database import engine
from utils.migration import load_db

app  = FastAPI()
models.base.metadata.create_all(bind=engine)
load_db()
app.include_router(pokemon_routes.router)
@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return "hi from fast api"