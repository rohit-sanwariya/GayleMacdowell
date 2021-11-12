class Node:
    def __init__(self,*args,**kwargs) -> None:
        self.next = None
        if(args):
            self.data = args[0]
        
            print(self.data)
        else:
            self.data = None
            print(self.data)
    

 



