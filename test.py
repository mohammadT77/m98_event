from datetime import datetime
from ticketing.models import *

e1 = manager.read(1, Event)

print("Events:", list(e1.get_all_tickets()))