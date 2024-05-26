from fastapi import FastAPI, Request
from routes import pokemon_routes
import data.models as models
from data.database import engine


app  = FastAPI()
models.base.metadata.create_all(bind=engine)

app.include_router(pokemon_routes.router)
@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return "hi from fast api"