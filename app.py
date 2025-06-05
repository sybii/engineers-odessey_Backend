# main.py
from fastapi import FastAPI
from asgi2wsgi import ASGI2WSGI

# Step 1: Create your FastAPI app
app = FastAPI()

# Step 2: Add your endpoints
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on PythonAnywhere!"}

# Step 3: Convert to WSGI app
wsgi_app = ASGI2WSGI(app)
