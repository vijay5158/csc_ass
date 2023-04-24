from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
