    


class Node:
    def __init__(self,*args,**kwargs) -> None:
        self.next = None
        if(args):
            self.data = args[0]
        
            
        else:
            self.data = None
            

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
    
    def append(self,d):
        newNode = Node(d)
        if(not self.head.data):
            self.head = newNode
        else:
            current = self.head
            while(current.next):
                current = current.next
            
            current.next = newNode
    
    def prepend(self,d):
        pass
    def display(self):
        current = self.head
        while(current):
            print(f"data: {current.data}")
            current = current.next
        
        
            
    
    



list = LinkedList ()
for x in range(10):
    list.append(x)
list.display()
