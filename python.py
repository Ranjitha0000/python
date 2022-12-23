class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.nref = None;    
        self.pref = None;    
             
class DoublyLinkedList:    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
             
    def addNode(self, data):    
        newNode = Node(data);    
             
        if(self.head == None):    
            self.head = self.tail = newNode;    
            self.head.nref = None;    
            self.tail.pref = None;    
        else:    
            self.tail.next = newNode;    
            newNode.nref = self.tail;    
            self.tail = newNode;    
            self.tail.pref = None;    
                 
    def display(self):    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            print(current.data),;    
            current = current.next;    
                 
dList = DoublyLinkedList();    
dList.addNode(1);    
dList.addNode(2);    
dList.addNode(3);    
dList.addNode(4);    
dList.addNode(5);    
      
dList.display();
