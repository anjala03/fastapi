from fastapi import APIRouter
from models.note import Note
from config.db import connection
from schemas.note import noteEntity, notesEntity
from typing import Union
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

note=APIRouter()
@note.get("/abc", response_class=HTMLResponse)
async def read_items(request: Request):
    docs= connection.Notes.notes.find({})
    newdocs=[]

    for doc in docs:
       print()
       newdocs.append({
           "id":doc.get('_id'),
           "title":doc.get('title'),
           "desc":doc.get('desc'),
            "important":doc.get('important') 
            })
    #    print(doc)
    return templates.TemplateResponse("index2.html", {"request": request, "newdocs":newdocs})

@note.get("/", response_class=HTMLResponse)
async def read_items_get(request: Request):
    docs= connection.Notes.notes.find({})
    newdocs=[]

    for doc in docs:
       print()
       newdocs.append({
           "id":doc.get('_id'),
           "title":doc.get('title'),
           "desc":doc.get('desc'),
            "important":doc.get('important') 
            })
    #    print(doc)
    return templates.TemplateResponse("index.html", {"request": request, "newdocs":newdocs})


@note.post("/")
async def create_item(request: Request):
    form= await request.form()
    # note=connection.Notes.notes.insert_one(dict(form))
    formDict =dict(form)
    formDict["important"] = "on" if bool(formDict.get("important")) == True else "off"
    print(formDict)
    note=connection.Notes.notes.insert_one(formDict)
    # return templates.TemplateResponse("index.html", {"request": request, "note":note}) 
    return {"Success":True}
    #def add_note(note: Note):
    #    inserted_note= connection.Notes.notes.insert_one(dict(note))
    #    return noteEntity (inserted_note)
