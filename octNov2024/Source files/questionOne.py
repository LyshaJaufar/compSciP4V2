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
            "jump": self.jump,
            "swim": self.swim,
            "run": self.run,
            "drive": self.drive
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

# EventItem Objects
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

# Create an instance for each of the characters: Tarz & Geni
Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

Points = {
    "Tarz": 0,
    "Geni": 0
}

for event in Group:
    # calculate percentage chance of completing event
    eventType = event.getType()
    difficulty = event.getDifficulty()

    chances = {
        "Tarz": Tarz.CalculateScore(eventType, difficulty),
        "Geni": Geni.CalculateScore(eventType, difficulty)
    }

    winner = max(chances, key=chances.get)

    if chances["Tarz"] == chances["Geni"]:
        print(event.getName(), "is a draw")
    else:
        Points[winner] += 1
        print(winner, "won")

if Points["Tarz"] > Points["Geni"]:
    print("Tarz won with", Points["Tarz"], "points")
elif Points["Geni"] > Points["Tarz"]:
    print("Geni won with", Points["Geni"], "points")
else:
    print("draw")


