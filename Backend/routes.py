from fastapi import APIRouter, HTTPException
from .crud import get_tasks, add_task, delete_task
from .schemas import Task
from .crud import add_task, get_tasks, delete_task
from .db import task_collection
from bson import ObjectId

router = APIRouter()

def doc_to_dic_convertor(doc):
    doc = dict(doc)
    doc["_id"] = str(doc["_id"])
    return dict(doc)

@router.get('/tasks', response_model=dict)
async def fetch_tasks():
    try:
        tasks = await get_tasks()
        response = [doc_to_dic_convertor(task) for task in tasks]
        return {'message': 'Tasks fetched succssfully', 'data':response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch tasks: {e}")

@router.post('/add_task', response_model=dict)
async def create_task(task: Task):
    try:
        task = task.model_dump()
        result = await add_task(task)
        inserted_task = await task_collection.find_one({"_id": result.inserted_id})
        response = doc_to_dic_convertor(inserted_task)
        return {'message': 'Task added successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Task creation failed: {e}")

@router.delete('/tasks/{task_id}', response_model=dict)
async def remove_task(task_id: str):
    try:
        result = await delete_task(task_id)
        if result:
            deleted_doc = await task_collection.find_one({'_id': ObjectId(task_id)})
        else:
            raise HTTPException(status_code=404, detail="Task not found")
        return {'message': 'Task deleted successfully', 'data': deleted_doc}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete task: {e}")
