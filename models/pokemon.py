from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    types: list
    height: int
    weight: int



