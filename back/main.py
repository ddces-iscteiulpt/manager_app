import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run("apps.app:app", host="localhost", port=8000, reload=True)
