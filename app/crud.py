from fastapi import APIRouter, HTTPException, Depends
from typing import List
from bson import ObjectId
from .models import Note
from .db import notes_collection
from .authkey import get_current_user

router = APIRouter()

@router.post("/", response_model=Note)
async def create_note(note: Note, current_user: str = Depends(get_current_user)):
    new_note = await notes_collection.insert_one(note.dict(exclude_unset=True))
    if new_note:
        created_note = await notes_collection.find_one({"_id": new_note.inserted_id})
        return created_note
    else:
        raise HTTPException(status_code=500, detail="Failed to create note")

@router.get("/", response_model=List[Note])
async def read_notes(current_user: str = Depends(get_current_user)):
    all_notes = await notes_collection.find().to_list(length=None)
    return all_notes

@router.get("/{note_id}", response_model=Note)
async def read_note(note_id: str, current_user: str = Depends(get_current_user)):
    note = await notes_collection.find_one({"_id": ObjectId(note_id)})
    if note:
        return note
    else:
        raise HTTPException(status_code=404, detail="Note not found")

@router.put("/{note_id}", response_model=Note)
async def update_note(note_id: str, updated_note: Note, current_user: str = Depends(get_current_user)):
    updated_data = updated_note.dict(exclude_unset=True)
    updated_result = await notes_collection.update_one({"_id": ObjectId(note_id)}, {"$set": updated_data})
    if updated_result.modified_count == 1:
        return updated_data
    else:
        raise HTTPException(status_code=404, detail="Note not found")

@router.delete("/{note_id}", response_model=Note)
async def delete_note(note_id: str, current_user: str = Depends(get_current_user)):
    deleted_note = await notes_collection.find_one_and_delete({"_id": ObjectId(note_id)})
    if deleted_note:
        return deleted_note
    else:
        raise HTTPException(status_code=404, detail="Note not found")
