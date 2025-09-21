from .db import task_collection
from bson import ObjectId

def get_tasks():
    task_list = task_collection.find()
    return task_list.model_dump()

def add_task(task: str):
    return task_collection.insert_one(task)

def delete_task(task_id: str):
    return task_collection.delete_one({"_id": ObjectId(task_id)})