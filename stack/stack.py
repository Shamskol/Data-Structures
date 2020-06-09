"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# STACK ARRAY IMPLEMENTATION
class Stack:
    def __init__(self):
      self.size = 0
      self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
     self.size = self.size + 1
     self.storage.append(value)

    def pop(self):
        if self.size == 0:
            print("IndexError: Pop from empty list")
        else:
         self.size = self.size - 1
         return self.storage.pop()






#STACK LINKED LIST IMPLEMENTATION
class Node:
    def  __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

        
class Stack:
    def __init__(self, node=None):
        self.size = 1 if node is not None else 0
        self.storage = []
        self.head = node
        self.tail = node

    def __len__(self):
        return self.size

    def push(self, value):
        self.size = self.size + 1
        # self.storage.append(value)
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail =  new_node

    def pop(self):
        if not self.tail:
            return None
        
        if not self.head.get_next():
            self.size -= 1
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        
        current_node = self.head
        
        while (current_node.next_node is not None):
            prev  = current_node
            current_node = current_node.next_node
        prev.next =  None
       