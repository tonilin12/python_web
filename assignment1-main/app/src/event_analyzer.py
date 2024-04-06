
from .file_storage import *
from .models import *
from typing import List
from collections import Counter
from pydantic import BaseModel


class EventAnalyzer:
    @classmethod
    def get_joiners_multiple_meetings_method(cls, events: List[Event]):
        joiner_counter = Counter(joiner.name for event in events for joiner in event.joiners)
        

        if len(joiner_counter)==0:
            return "No joiners attending at least 2 meetings"

        return str(joiner_counter)




data= EventFileManager.read_events_from_file()
events = [Event(**item) for item in data]
EventAnalyzer.get_joiners_multiple_meetings_method(events)    
