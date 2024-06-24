from fastapi import FastAPI, Request
from routes import pokemon_routes
from routes import evolve_routes
from routes import trainer_routes
from routes import images_routes
from classes.requests_handler import requests_handler


async def lifespan(app: FastAPI):
    print(requests_handler.data_migration())
    yield
    
app  = FastAPI(lifespan=lifespan)


app.include_router(pokemon_routes.router)
app.include_router(trainer_routes.router)
app.include_router(evolve_routes.router)
app.include_router(images_routes.router)


@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return "hi from fast api"