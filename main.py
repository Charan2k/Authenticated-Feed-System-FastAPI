from pydoc import render_doc
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {'data':{'name':'charan'}}