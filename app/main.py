import json
import uvicorn
from fastapi import FastAPI
from routers import router


app = FastAPI()
app.include_router(router, prefix='/api')


if __name__ == '__main__':
    """
    This is the main module of the application.

    It creates a FastAPI instance, includes the router for the API endpoints,
    and runs the application using Uvicorn server on host '0.0.0.0' and port 8000.
    """
    uvicorn.run(app, host='0.0.0.0', port=8000)
