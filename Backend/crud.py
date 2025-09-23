from .db import task_collection
from bson import ObjectId

def get_tasks():
    task_list = task_collection.find()
    return list(task_list)

def add_task(task):
    return task_collection.insert_one(task)

def delete_task(task_id: str):
    return task_collection.delete_one({"_id": ObjectId(task_id)})