from datetime import datetime
from dataclasses import dataclass
import os
from data_manager import BaseModel, FileManager

manager = FileManager({'ROOT_PATH':'data/'})

@dataclass
class ManagerUser(BaseModel):
    name: str
    username: str
    password: str

    @classmethod
    def login(cls, username, password):
        user = list(manager.read_all(cls))
        user = user[0] if user else None
        assert user, "Manager user is not set"

        return user.username == username and user.password == password




class Event(BaseModel):
    title: str
    capacity: int
    event_date: datetime

    def __init__(self, title, capacity, event_date) -> None:
        self.title = title
        self.capacity = capacity
        self.event_date = event_date
    
    def __repr__(self) -> str:
        return f"<Event #{self._id}>"

    def __str__(self):
        return f"Event #{self._id}: {self.title} - {self.event_date}"

    def get_all_tickets(self):
        return filter(
            lambda ticket: ticket.event._id == self._id,
            manager.read_all(Ticket)
        )

    @property
    def reserved(self):
        all_quanitities = map(lambda ticket: ticket.quantity, self.get_all_tickets())
        return sum(all_quanitities)

    @property
    def availability(self):
        return self.capacity - self.reserved

@dataclass
class Ticket(BaseModel):
    event: Event
    customer_id: str
    quantity: int = 1