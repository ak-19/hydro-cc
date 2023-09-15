class Datapoint:
    def __init__(self, timestamp: int, value: int):
        self.timestamp = timestamp
        self.value = value

    def __eq__(self, other):
        return self.timestamp == other.timestamp
    
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __gt__(self, other):
        return self.timestamp > other.timestamp
    
    def __le__(self, other):
        return self.timestamp <= other.timestamp
    
    def __ge__(self, other):
        return self.timestamp >= other.timestamp
    
    def __ne__(self, other):
        return self.timestamp != other.timestamp
    
    def __str__(self):
        return f'Value: {self.value}, Timestamp: {self.timestamp}'