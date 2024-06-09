from pydantic import BaseModel

class Trainer(BaseModel):
    name: str
    town: str

