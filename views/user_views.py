from fastapi import APIRouter, Depends, HTTPException
from database import user_collection
from models.user_model import User
from typing import Optional
from schemas.user_schema import user_serializer,users_serializer
from bson import ObjectId

router = APIRouter()

@router.post("/",response_model=User)
async def create_user(user:User):
    user_dict = user.dict()
    result = user_collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

@router.get("/", response_model=dict)
async def get_users(name: Optional[str] = None, skip: int = 0, limit: int = 10):
    query = {}
    if name:
        query = {"name": {"$regex": f".*{name}.*", "$options": "i"}}
    total_records = user_collection.count_documents(query)
    users = list(user_collection.find(query).skip(skip).limit(limit))
    data = users_serializer(users)
    return {"users": data, "total_records": total_records}

@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        data = user_serializer(user)
        return data
    else:
        raise HTTPException(status_code=404, detail="User not found")
