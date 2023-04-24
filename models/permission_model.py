from pydantic import BaseModel

class Permission(BaseModel):
    user_id: str
    org_name: str
    access_level: str