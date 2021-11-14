import random as ran

class Node:
    def __init__(self,*args) -> None:
        self.next = None
        if(args):
            self.data = args[0]
        else:
            self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        
    
    def display(self):
        
        current = self.head
        while(current.next):
            print(current.data,end=" ")
            current = current.next
        print(end="\n")
    def append(self,d):
        if(not self.head):
            self.head.data = d
        else:
            newNode = Node(d)
            newNode.next = self.head
            self.head = newNode
    
    def removeDupes(self):
        listSet = set()
        previous = Node()
        cNext = Node()
        cNext = self.head
        while(cNext.next):
            if(cNext.data in listSet):
                previous.next = cNext.next
            else:
                listSet.add(cNext.data)
                previous = cNext
            cNext = cNext.next
    def removeDupesNobuffer(self):
        current = self.head
        runner = Node()
        while(current.next):
            runner = current
            while(runner.next.next):
                if(runner.next.data == current.data):
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        
        
        
        
        



    
    
    

    
  

listLink = LinkedList()
for x in range(10):
    listLink.append(ran.randint(12,20))
listLink.display()

listLink.removeDupesNobuffer()

listLink.display()



