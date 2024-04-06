from fastapi import APIRouter, HTTPException
from typing import List
from .models import Event
from .event_analyzer import *
from .file_storage import *
from typing import List, Optional
from pydantic import BaseModel
from starlette.responses import JSONResponse 

router = APIRouter()



@router.get("/events", response_model=List[Event])
async def get_all_events(): 
    all_events = EventFileManager.read_events_from_file()
    return all_events


@router.get("/events/filter", response_model=List[Event])
async def get_events_by_filter(date: str = None, organizer: str = None, status: str = None, type: str = None):
    all_events = EventFileManager.read_events_from_file()

    filtered_events = all_events

    if date:
        filtered_events = [event for event in filtered_events if event['date'] == date]

    if date:
        filtered_events = [event for event in filtered_events if event['organizer']['name'] == date]

    if status:
        filtered_events = [event for event in filtered_events if event['status'] == status]

    if type:
        filtered_events = [event for event in filtered_events if event['type'] == type]

    return filtered_events



@router.get("/events/{event_id}", response_model=Event)
async def get_event_by_id(event_id: int):
    all_events = EventFileManager.read_events_from_file()

    for event in all_events:
        if event['id'] == event_id:
            return event
    
    raise HTTPException(status_code=404, detail="Event not found")



@router.post("/create_event/")
async def create_event(event: Event):
    try:
        events = EventFileManager.read_events_from_file()

        # Check if the event ID already exists
        for existing_event in events:
            if existing_event["id"] == event.id:
                raise HTTPException(status_code=400, detail="Event already exists")

        EventFileManager.write_events_to_file(event0=event)

        return  ("Event with id ",event.id," created successfully")

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})






@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: Event):
    try:
        events = EventFileManager.read_events_from_file()

        n=None
        for existing_event in events:
            if existing_event["id"] == event.id:
                n=events.index(existing_event)
        if n is False:
            raise HTTPException(status_code=400, detail="Event does not exists")
        else:
            original_id=events[n]['id']
            EventFileManager.write_events_to_file(event,n)
            
            events=EventFileManager.read_events_from_file()
            
            v=None
            for event in events:
                if event['id']==original_id:
                    v=event
            return v

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})



@router.delete("/events/{event_id}")
async def delete_event(event_id: int):
    try:
        events = EventFileManager.read_events_from_file()

        n=None
        for existing_event in events:
            if existing_event["id"] ==event_id:
                n=events.index(existing_event)
        if n is None:
            raise HTTPException(status_code=400, detail="Event does not exist")

        deleted_item=events[n]
        EventFileManager.write_events_to_file(n=n)
        events2=EventFileManager.read_events_from_file()
        
        b=True
        for item in events2:
            if(item==deleted_item):
                b=False
        
        if b:
            return "item with id ",event_id," delete successful"
        else:
            return "delete failed"


    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})



@router.get("/events/joiners/multiple-meetings")
async def get_joiners_multiple_meetings():
    data= EventFileManager.read_events_from_file()
    events = [Event(**item) for item in data]
    return EventAnalyzer.get_joiners_multiple_meetings_method(events)    



