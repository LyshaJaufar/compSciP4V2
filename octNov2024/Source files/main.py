class EventItem:
    def __init__(self, EventName, Type, Difficulty):
        self.EventName = EventName
        self.Type = Type
        self.Difficulty = Difficulty

    def getName(self):
        return self.EventName
    
    def getDifficulty(self):
        return self.Difficulty

    def getType(self):
        return self.Type
    
Group = []