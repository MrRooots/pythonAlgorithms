# Simple stack implementation
class Stack:
  data = None
  length = None

  def __init__(self) -> None:
    self.data = []
    self.length = 0

  def is_empty(self) -> bool:
    return not self.length

  def is_not_empty(self) -> bool:
    return not self.is_empty()

  def peek(self) -> any:
    return self.data[-1]

  # Delete the element from the top
  def pop(self) -> any:
    if self.is_not_empty():
      self.length -= 1
      return self.data.pop()

  # Add element to the top
  def add(self, element) -> None:
    self.length += 1
    self.data.append(element)

  def clear(self) -> None:
    self.data.clear()
