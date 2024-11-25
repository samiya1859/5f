import uuid

class Destination:
    def __init__(self, name, description, location, price, added_by):
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.name = name
        self.description = description
        self.location = location
        self.price = price
        self.added_by = added_by  # Email of the admin who added this

# In-memory storage for destinations
destinations = {}
