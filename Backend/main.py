from fastapi import FastAPI, HTTPException
from typing import List
from .schemas import Task
from .crud import add_task, get_tasks, delete_task
from .db import task_collection
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or ["http://localhost:5173"] if using Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def doc_to_dic_convertor(doc):
    doc = dict(doc)
    doc["_id"] = str(doc["_id"])
    return dict(doc)

@app.get('/')
def root():
    try:
        return {'status': 'healthy', 'message': 'FastAPI running succcessfully!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Internal server error: {e}')
        

@app.post('/add_task', response_model=dict)
def create_task(task: Task):
    try:
        task = task.model_dump()
        result = add_task(task)
        inserted_task = task_collection.find_one({"_id": result.inserted_id})
        response = doc_to_dic_convertor(inserted_task)
        return {'message': 'Task added successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Task creation failed: {e}")

@app.get('/tasks', response_model=dict)
def fetch_tasks():
    try:
        tasks = get_tasks()
        response = [doc_to_dic_convertor(task) for task in tasks]
        return {'message': 'Tasks fetched succssfully', 'data':response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch tasks: {e}")

@app.delete('/tasks/{task_id}', response_model=dict)
def remove_task(task_id: str):
    try:
        result = delete_task(task_id)
        if result:
            deleted_doc = task_collection.find_one({'_id': ObjectId(task_id)})
        else:
            raise HTTPException(status_code=404, detail="Task not found")
        return {'message': 'Task deleted successfully', 'data': deleted_doc}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete task: {e}")


