import json
import os
from collections import OrderedDict

class EventFileManager:

    
    current_file_location = os.path.realpath(__file__)

    target_directory = os.path.abspath(
        os.path.join(current_file_location, '..', '..', '..'))

    FILE_PATH = os.path.join(target_directory, 'event.json')
    events=None
    
    @classmethod
    def read_events_from_file(cls,path0=None):
    
        try:
            path=cls.FILE_PATH
            if path0 is not None:
                path=path0
            with open(path, 'r') as file:
                events0 = json.load(file)
                cls.events=events0
                return cls.events
                #print(events)
                
        except Exception as e:
            print("Error reading events file:", e)


    @classmethod
    def write_events_to_file(cls, event0=None,n=None):
        try:
            with open(cls.FILE_PATH, 'r+') as file:
                cls.events=cls.read_events_from_file()
                if n is not None:
                    del cls.events[n]
                if event0 is not None:
                    cls.events.append(event0.to_dict()) 

                file.seek(0)
                file.truncate(0)


                json.dump(cls.events,file,indent=4)
                
        except Exception as e:
            print("Error writing events to file:", e)

