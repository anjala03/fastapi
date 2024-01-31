from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# sets the connection with the database
connection= MongoClient("mongodb+srv://anjalamongodb:mongodb@cluster0.b3vxizb.mongodb.net/Notes")

#@app.get("/")
#def read_root():
#    return {"Hello": "World"}
@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    
    docs= connection.Notes.notes.find({})
    newdocs=[]

    for doc in docs:
       newdocs.append({
           "id":doc["_id"],
           "note":doc["note"]

       })
       print(doc)
    return templates.TemplateResponse("index.html", {"request": request, "newdocs":newdocs})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}