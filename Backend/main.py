from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as task_router

app = FastAPI()

app.include_router(task_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] if using Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    try:
        return {'status': 'healthy', 'message': 'FastAPI running succcessfully!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Internal server error: {e}')