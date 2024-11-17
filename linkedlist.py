class priorityQueueNode:
    def __init__(self, value, pr):
        self.date = value
        self.priority = pr
        self.next = None
class priorityQueue:
    def _init__(self):
        self.front = None
    
    def isEmpty(self):
        return True if self.front == None else False
    def push(self, value,priority):
        if self.isEmpty() == True:
            self.front = priorityQueueNode(value, priority)
        else:
            if self.front.priority > priority:
                newNode = priorityQueueNode(value, priority)
                newNode.next = self.front
                self.front = newNode
            else:
                temp = self.front
                while temp.next:
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                newNode = priorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode
    


