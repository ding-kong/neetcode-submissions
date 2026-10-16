class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        curr = self.head

        for _ in range(index):
            curr = curr.next
        
        return curr.val
        

    def insertHead(self, val: int) -> None:
        curr = Node(val=val)
        curr.next = self.head
        self.head = curr
        self.size += 1
        if self.size <= 1:
            self.tail = self.head
        
    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.insertHead(val)
            return
        p = Node(val)
        self.tail.next = p
        self.tail = p
        self.size += 1
        
    def remove(self, index: int) -> bool:
        if self.size <= index:
            return False
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return True
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        
        p, p_prev = self.head, None
        
        for _ in range(index):
            p, p_prev = p.next, p
            
        p_prev.next = p.next
        
        if p == self.tail:
            self.tail = p_prev

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        p = self.head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        return lst
