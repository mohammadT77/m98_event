from datetime import datetime
from dataclasses import dataclass
import os
from abc import ABC, abstractclassmethod, abstractmethod


class BaseModel(ABC):

    def save_file(self):
        with open(self.get_file_path(), 'wt') as f:
            f.write(self.get_file_content())

    @abstractmethod
    def get_file_path(self):
        pass

    @abstractmethod
    def get_file_content(self) -> str:
        pass

    @abstractclassmethod
    def from_str(cls, s: str):
        pass

    @classmethod
    def from_path(cls, path: str):
        with open(path, 'r') as f:
            return cls.from_str(f.read())

    @abstractclassmethod
    def get_all_path(cls) -> list[str]:
        pass

    @classmethod
    def get_all(cls):
        return map(cls.from_path, cls.get_all_path())


    def delete(self):
        os.remove(self.get_file_path())

class ManagerUser(BaseModel):
    pass

class Event(BaseModel):
    id: int
    title: str
    capacity: int
    # reserved: int
    event_date: datetime

    def __init__(self, id, title, capacity, event_date) -> None:
        self.id = id
        self.title = title
        self.capacity = capacity
        self.event_date = event_date
    
    def get_file_path(self):
        return f'{self.id}.event'
    
    def get_file_content(self) -> str:
        return f"{self.id}||{self.title}||{self.capacity}||{self.event_date}"
    
    @classmethod
    def from_str(cls, s: str):
        id, title, cap, event_date = s.split('||')
        return cls(int(id), title, int(cap), datetime.fromisoformat(event_date))
    
    @classmethod
    def get_all_path(cls) -> list[str]:
        return [path for path in os.listdir() if path.endswith('.event')]
    
    @classmethod
    def find_by_id(cls, id):
        for e in cls.get_all():
            if e.id == id:
                return e
        assert None, "Not found" # AssertionError

    def __repr__(self) -> str:
        return f"<Event #{self.id}>"

    def __str__(self):
        return f"Event #{self.id}: {self.title} - {self.event_date}"


@dataclass
class Ticket(BaseModel):
    id: int  # for behanam
    event: Event
    customer_id: str
    quantity: int = 1

    def get_file_path(self):
        return f'{self.id}.ticket'
    
    def get_file_content(self) -> str:
        return f"{self.id}:{self.event.id}:{self.customer_id}:{self.quantity}"
    
    @classmethod
    def from_str(cls, s: str):
        id, event_id, customer_id, quantity = s.split(':')
        event = Event.find_by_id(event_id)
        return cls(int(id), event, customer_id, int(quantity))
    
    @classmethod
    def get_all_path(cls) -> list[str]:
        return [path for path in os.listdir() if path.endswith('.ticket')]
    
    @classmethod
    def find_by_id(cls, id):
        for e in cls.get_all():
            if e.id == id:
                return e
        assert None, "Not found" # AssertionError


