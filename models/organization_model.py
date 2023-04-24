from pydantic import BaseModel


class Organization(BaseModel):
    name: str

    class Config:
        arbitrary_types_allowed = True
