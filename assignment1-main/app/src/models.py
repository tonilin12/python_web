from typing import List, Optional
from pydantic import BaseModel


class Organizer(BaseModel):
    name:str
    email: str


class Joiner(BaseModel):
    name: str
    country: str
    email:str


class Event(BaseModel):
    id: Optional[int]
    name: str
    date: str
    organizer: Organizer
    status: str
    max_attendees: int
    joiners: Optional[List[Joiner]]
    location: str
    type:str
    status:str
    
 
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'organizer': self.organizer.dict(), 
            'status': self.status,
            'type':self.type,
            'joiners': [joiner.dict() for joiner in self.joiners] if self.joiners else None,  
            'location': self.location,
            'max_attendees': self.max_attendees,  

        }


