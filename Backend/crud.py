from .db import task_collection
from bson import ObjectId

async def get_tasks():
    return await task_collection.find().to_list(length=None)

async def add_task(task):
    return await task_collection.insert_one(task)

async def delete_task(task_id: str):
    return await task_collection.delete_one({"_id": ObjectId(task_id)})