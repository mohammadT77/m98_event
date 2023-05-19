from datetime import datetime
# from dataclasses import dataclass


class ManagerUser:
    pass

class Event:
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

    
    def save_file(self):
        with open(self.get_file_path(), 'wt') as f:
            f.write(self.get_file_content())

    def get_file_path(self):
        return f'{self.id}.event'


    def get_file_content(self) -> str:
        return f"{self.id}||{self.title}||{self.capacity}||{self.event_date}"

    @classmethod
    def from_file_content(cls, s: str):
        # s = 1||akbar||10||20222.22.2.2.2.
        # [1, akbar, 10, 22....]
        id, title, cap, event_date = s.split('||')
        return cls(int(id), title, int(cap), datetime.fromisoformat(event_date))


    

class Ticket:
    pass