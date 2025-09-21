from fastapi import FastAPI, HTTPException
from .schemas import Task
from .crud import add_task, get_tasks, delete_task
from .db import task_collection
from bson import ObjectId

app = FastAPI()

def doc_to_dic_convertor(doc):
    doc["_id"] = str(doc["_id"])
    return {**doc}

@app.get('/')
def root():
    try:
        return {'status': 'healthy', 'message': 'FastAPI running succcessfully!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Internal server error: {e}')
        

@app.post('/add_task', respomse_model=Task)
def create_task(task: str):
    try:
        result = add_task(task)
        inserted_task = task_collection.find({"_id": result.inserted_id})
        response = doc_to_dic_convertor(inserted_task)
        return {'message': 'Task added successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Task creation failed: {e}")

@app.get('/tasks', response_model=list[Task])
def fetch_tasks():
    try:
        tasks = get_tasks()
        response = [doc_to_dic_convertor(task) for task in tasks]
        return {'message': 'Tasks fetched succssfully', 'data':response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch tasks: {e}")

@app.delete('/tasks/{task_id}', response_model=str)
def remove_task(task_id: str):
    try:
        result = delete_task(task_id)
        if result:
            deleted_doc = task_collection.find({'_id': ObjectId(task_id)})
        else:
            raise HTTPException(status_code=404, detail="Task not found")
        return {'message': 'Task deleted successfully', 'data': deleted_doc}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete task: {e}")


