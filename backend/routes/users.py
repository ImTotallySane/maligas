from fastapi import APIRouter, HTTPException
from ..models import User
from bson import ObjectId

router = APIRouter()

# Helper function to get the users collection
async def get_users_collection():
    from db import init_db
    return init_db()["users_collection"]

# Get all users
@router.get("/")
async def get_users():
    collection = await get_users_collection()
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)
    return users

# Create a new user
@router.post("/")
async def create_user(user: User):
    collection = await get_users_collection()
    # Insert the new user into the users collection
    result = await collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

# Delete a user by their user_id
@router.delete("/{user_id}")
async def delete_user(user_id: str):
    collection = await get_users_collection()
    # Ensure the user_id is converted to an ObjectId before deletion
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    
    if result.deleted_count:
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="User not found")
