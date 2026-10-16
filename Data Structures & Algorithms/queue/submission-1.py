class Node:
  def __init__(self, val, prev=None, nxt=None):
    self.value = val
    self.prev = prev
    self.nxt = nxt


class Deque:
    def __init__(self):
      self.left = None
      self.right = None
      self.size = 0

    def isEmpty(self) -> bool:
      print(self.size, self.left)
      return self.size == 0

    def append(self, value: int) -> None:
      curr = Node(value)
      if self.size == 0:
        self.right = curr
        self.left = curr
        self.size = 1
        return

      self.right.nxt = curr
      curr.prev = self.right
      self.right = curr
      self.size += 1

    def appendleft(self, value: int) -> None:
        curr = Node(value)
        
        if self.size == 0:
          self.right = curr
          self.left = curr
          self.size = 1
          return

        self.left.prev = curr
        curr.nxt = self.left
        self.left = curr
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
          return -1
        if self.size == 1:
          val = self.left.value
          self.right = None
          self.left = None
          self.size = 0
          return val
        val = self.right.value
        prev = self.right.prev
        prev.nxt = None
        self.right = prev
        self.size -= 1
        return val

    def popleft(self) -> int:
        if self.size == 0:
          return -1
        if self.size == 1:
          val = self.left.value
          self.right = None
          self.left = None
          self.size = 0
          return val
        val = self.left.value
        nxt = self.left.nxt
        nxt.prev = None
        self.left = nxt
        self.size -= 1
        return val
