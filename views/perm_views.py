from fastapi import APIRouter, Depends, HTTPException
from database import perm_collection
from models.permission_model import Permission
from typing import Optional
from schemas.user_schema import user_serializer,users_serializer
from bson import ObjectId

router = APIRouter()


# Permission API endpoints
@router.post("/")
async def create_permissions(perm: Permission):
    perm_dict = perm.dict()
    result = perm_collection.insert_one(perm_dict)
    perm_dict["_id"] = str(result.inserted_id)
    return perm_dict

@router.put("/{perm_id}")
async def update_permissions(perm_id: str, perm: Permission):
    result = perm_collection.update_one({"_id":ObjectId(perm_id)}, {"$set": perm})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Permission not found")
    return {"msg":"Permission updated successfully"}

@router.delete("/{perm_id}")
async def delete_permissions(perm_id: str):
    result = perm_collection.delete_one({"_id": ObjectId(perm_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Permission not found")
    return {"msg":"Permission deleted successfully"}
