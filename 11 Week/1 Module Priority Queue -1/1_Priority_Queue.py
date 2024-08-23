class PriorityQueueNode:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority


class PirorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value

    def __percolatUp(self):
        pass

    def __percolateDown(self):
        pass

    def insert(self, value, priority):
        pass

    def removeMin(self):
        pass
