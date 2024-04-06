import requests
import json
from file_storage import *
from models import *
import random


def get_all_event_test():
    print("get_all_event_test()")
    url = 'http://localhost:8000/events'

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")


def filter_test():
    print("\nfilter-test")
    url = 'http://localhost:8000/events/filter'

    params = {
        'id': 1,  
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")


def get_by_id_test():
    print("\ngetByIdTest")
    event_id = 1 

    url = f'http://localhost:8000/events/{event_id}'

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    elif response.status_code == 404:
        print("Event not found.")
    else:
        print(f"Error: {response.status_code}")


v0=10
def create_event_test():
    print("\ncreate_event_test")
    events=EventFileManager.read_events_from_file()

    url = 'http://localhost:8000/create_event/'
    
    events[0]['id']=random.randint(100,200)
    response = requests.post(url, json=events[0])

    print(response.text)
    

def update_event_test():
    print("\nupdate_event_test")
    events=EventFileManager.read_events_from_file()
    events[0]['name']+="X"
    event_id=events[0]['id']
    url = f'http://localhost:8000/events/{event_id}'



    response = requests.put(url, json=events[0])

    print(response.text)
    
    
def delete_event_test():
    print("\ndelete_event_test")
    events=EventFileManager.read_events_from_file()
    event_id=events[0]['id']
    print(event_id)
    url = f'http://localhost:8000/events/{event_id}'

    events[0]['id']=events[0]['id']

    response = requests.delete(url)

    print(response.text)



def multiple_joiner_test():
    print("\multiple_joiner_test")
    url = "http://localhost:8000/events/joiners/multiple-meetings"


    response = requests.get(url)

    print(response.text)
    
create_event_test()
create_event_test()
delete_event_test()



















