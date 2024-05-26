from pydantic import BaseModel



class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    height: int
    weight: int



