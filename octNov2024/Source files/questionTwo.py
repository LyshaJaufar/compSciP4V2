

class Queue:
    def __init__(self, headPointer, tailPointer):
        self.queueArray = []
        for i in range(100):
            self.queueArray.append(-1)
        self.headPointer = headPointer # points to the index of the first daa item
        self.tailPointer = tailPointer # points to the index of the next free location

def Enqueue(AQueue, TheData):
    if AQueue.headPointer == -1:
        AQueue.headPointer = 0
        AQueue.tailPointer += 1
        return 1
    
    if AQueue.tailPointer > 99:
        return -1
    
    else:
        AQueue.queueArray[AQueue.tailPointer] = TheData
        AQueue.tailPointer = AQueue.tailPointer
        return 1
    

def returnAllData(AQueue):
    concatenatedVals = ""
    if AQueue.headPointer == -1:
        return None
    else:
        for i in range(AQueue.headPointer, len(AQueue.queueArray)):
            concatenatedVals += str(AQueue.queueArray[i]) + " "
    return concatenatedVals


TheQueue = Queue(-1, 0)
print(returnAllData(TheQueue))
