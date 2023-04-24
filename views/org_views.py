from fastapi import APIRouter, Depends,HTTPException
from typing import Optional
from database import org_collection
from models.organization_model import Organization
from schemas.org_schema import orgs_serializer,org_serializer

router = APIRouter()

# Organization API endpoints
@router.post("/")
async def create_organization(org: Organization):
    org_data = org.dict()
    org_exists = org_collection.find_one({"name": org_data["name"]})
    if org_exists:
        raise HTTPException(status_code=400, detail="Organization with same name already exists")
    result = org_collection.insert_one(org_data)
    org_data["_id"] = str(result.inserted_id)
    return org_data

@router.get("/")
async def get_organizations(name: Optional[str] = None, skip: int = 0, limit: int = 10):
    query = {}
    if name:
        query = {"name": {"$regex": f".*{name}.*", "$options": "i"}}
    total_records = org_collection.count_documents(query)
    orgs = list(org_collection.find(query).skip(skip).limit(limit))
    data = orgs_serializer(orgs)
    return {"organizations": data, "total_records": total_records}

@router.get("/{org_name}")
async def get_organization(org_name: str):
    org = org_collection.find_one({"name": org_name})
    if org:
        data = org_serializer(org)
        return data
    else:
        raise HTTPException(status_code=404, detail="User not found")
