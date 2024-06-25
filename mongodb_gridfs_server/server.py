from fastapi import FastAPI, Request
from routes import images_routes
app  = FastAPI()


app.include_router(images_routes.router)

@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return "Welcome to Pokemons World"