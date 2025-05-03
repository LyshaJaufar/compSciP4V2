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
    
class Character:
    # Attribute declarations
    def __init__(self, characName, jump, swim, run, drive):
        self.characName = characName
        self.jump = jump                      
        self.swim = swim                     
        self.run = run                    
        self.drive = drive       

    def GetName(self):
        return self.characName

    def CalculateScore(self, eventType, difficulty):
        skillsMap = {
            "jump": self.__jump,
            "swim": self.__swim,
            "run": self.__run,
            "drive": self.__drive
        }

        successTable = {
            1: 80,
            2: 60,
            3: 40,
            4: 20
        }

        skillLevel = skillsMap[eventType]

        if skillLevel >= difficulty:
            return  100
        else: 
            difference = difficulty - skillLevel
            return successTable[difference]


Group = []

# Data for the events
events = [
    ("Bridge", "jump", 3),
    ("Water wade", "swim", 4),
    ("100 mile run", "run", 5),
    ("Gridlock", "drive", 2),
    ("Wall on wall", "jump", 4)
]

for name, event_type, difficulty in events:
    Group.append(EventItem(name, event_type, difficulty))

