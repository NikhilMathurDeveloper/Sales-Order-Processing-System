class node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
class priority():
    def __init__(self):
        self.head = None
    def empty(self):
        return True if self.head ==None else False
    def insert(self, data, priority):
      
        if self.empty() == True:
            self.head = node(data, priority)
        else:
            if self.head.priority > priority:
                new_node = node(data, priority)
                new_node.next = self.head
                self.head = new_node
 
            else:
                current = self.head
                while current.next:
                    if priority <= current.next.priority:
                        break
                    current = current.next
                new_node = node(data, priority)
                new_node.next = current.next
                current.next = new_node
    def printLinked(self):
        if self.empty():
            print("not valid")
        else:
            current = self.head
            while current:
                print(current.data, end= " ")
                current = current.next
           



pq = priority()
pq.insert(4,1)
pq.insert(5,2)

pq.insert(6,3)
pq.insert(7,0)

h = pq.printLinked()
print(h)






        
  
