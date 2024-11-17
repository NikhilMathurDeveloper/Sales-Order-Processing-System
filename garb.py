class node:
                    def __init__(self, data, priority):
                        self.data = data
                        self.priority = priority 
                        self.next = None
                class linkedList:
                    def __init__(self):
                        self.head = None
                    def prepend(self, data, priority):#Prepend data
                        new_node = node(data, priority)
                        current = self.head
                        new_node.next = self.head
                        if not self.head:
                            new_node.next = new_node
                        else:
                            while current.next != self.head:
                                current = current.next
                            current.next = new_node
                        self.head = new_node
                    def getPriority(self):#Gets priority 
                        return self.priority
                
                    def append(self, data, priority):#Appends data
                        if not self.head:
                            self.head = node(data, priority)
                            self.head.next = self.head
                        else:
                            new_node = node(data, priority)
                            current = self.head
                            while current.next != self.head:
                                current=current.next
                            current.next = new_node
                            new_node.next = self.head        
                    def printList(self):#Prints linked list
                        current = self.head
                        arr = []
                        while current:
                            arr.append(current.data)
                            current = current.next
                            if current == self.head:
                                break   
                        #print(arr)
                        return arr
                    def printList1(self):
                        
                        
                          
                    
                     
                        #with open('object.pickle', 'rb') as f:
                            #p1 = pickle.load(f)


                        arr = []
                        current = self.head
                    
                        while current:
                            #p1.append(current.data)
                            current = current.next
                            if current == self.head:
                                break 
                        #with open('object.pickle', 'wb') as f:
                            #pickle.dump(p1, f)
                
                        #return p1

                        
                    def insert(self, data, priority):#Inserts into specific section in linked list: according to priority 
                        new_node = node(data, priority)
                        current = self.head

                        while current.next != None and current.next.priority < new_node.priority:
                            current = current.next
                        new_node.next = current.next
                        current.next = new_node
                    def remove(self):#Removes node

                        current = self.head
                        while current.next != self.head:
                           current = current.next
                        current.next = self.head.next
                        self.head = self.head.next
 
                    def priority(self, data, priority):#Appends, prepends, and inserts accoridng to priority of node.
                        current = self.head
                        new_node = node(data, priority)
                        
                        if current == None:
                            self.append(new_node.data, new_node.priority)
                            
                        
                        else:
                            if new_node.priority < current.priority:
                                self.prepend(new_node.data, new_node.priority)
                            while current.next != self.head:
                                last = current
                                current = current.next
                            if new_node.priority > last.priority and new_node.priority < current.priority:
                                self.insert(new_node.data, new_node.priority)
                        
                                    

                            prior = current.priority
          

                            if new_node.priority > prior:
                                self.prepend(new_node.data, new_node.priority)
                    
                 
                    

          

