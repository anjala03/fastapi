def noteEntity(item) -> dict:
    #this means that the function Note which takes one paramter "item" will return the value as dictionary
    return {

        "id":str (item["_id"]), 
        "title": item ["title"], 
        "desc": item ["desc"], 
        "important": item ["important"]
    }
def notesEntity(items) -> list:
    # return [noteEntity(item) for item in items]
    all = []
    for item in items:
        all.append(noteEntity(item))
    return all