import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


class PriorityQueueWithFunction(PriorityQueue):
    # priorityFunction(item) -> priority
    def __init__(self, priority_function):
        self.priority_function = priority_function
        PriorityQueue.__init__(self)  # super-class call

    def push(self, item, **kwargs):
        # Adds an item to the Queue with priority from the priority function
        PriorityQueue.push(self, item, self.priority_function(item))
