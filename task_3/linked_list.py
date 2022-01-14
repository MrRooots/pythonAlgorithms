"""
Написать  программу,  реализующую  основные  операции  над  линейными списками:
  + добавление нового элемента в список
  + поиск заданного элемента в списке
  + удаление заданного элемента из списка
  + вывод списка на экран
  + удаление всего списка с освобождением памяти

  + удалить из списка все повторяющиеся элементы
"""

import random as random


# Linked list node
class LinkedListNode:
  value = None  # Value of this node [any]
  next = None   # 'Pointer' to the next [LinkedListNode]

  # Constructor
  def __init__(self, value: any, next_node=None) -> None:
    self.value = value
    self.next = next_node


class LinkedList:
  length = 0   # Length of the list
  head = None  # Head of the linked list

  # Constructor
  def __init__(self, first_node: LinkedListNode = None) -> None:
    self.head = first_node

  # Delete all list nodes
  def __del__(self) -> None:
    # Unlinked elements will be deleted by garbage collector
    while self.head:
      self.head = self.head.next

  # Add element to a linked list { list + element || list + [e1, e2, ...] || list + e1 + e2 || list += e}
  def __add__(self, items: any):
    if isinstance(items, list) or isinstance(items, set) or isinstance(items, tuple):
      self.length += len(items)  # Increase the length of the list
      items = [LinkedListNode(value=item) for item in items]  # Convert item to list node
    else:
      self.length += 1  # Increase the length of the list
      items = [LinkedListNode(value=items)]  # Convert item to list node

    if self.head:
      current = self.head

      # Move till the end of the list
      while current.next:
        current = current.next

      for element in items:
        current.next = element
        current = current.next

    else:
      current = items[0]
      self.head = current

      for element in items[1::]:
        current.next = element
        current = current.next

    return self

  # Print the list to console { print(list_instance) }
  def __str__(self) -> str:
    if self.head:
      result = '['
      current = self.head

      while current:
        result += str(current.value) + (', ' if current.next else ']')
        current = current.next

      return result

    else:
      return 'Linked list is empty! Use {+} to add elements to list!'

  # Get element from list by given `index`: { list[index] = item from list on that index }
  def __getitem__(self, index: int) -> any:
    if index > self.length:
      raise IndexError('List index out of range!')

    current = self.head
    current_index = 0

    while current and current_index != index:
      current_index += 1
      current = current.next

    return current.value

  # Get the index of given element { list.index_of(element) }
  def index_of(self, element: any) -> int:
    index = 0
    current = self.head

    while current:
      if current.value == element:
        return index
      else:
        current = current.next
        index += 1

    raise ValueError('{} is not in list'.format(element))

  # Remove first element from list matched to given value
  def remove_by_value(self, value: any) -> bool:
    previous = None
    current = self.head

    while current:
      if current.value == value:
        if previous:
          previous.next = current.next
        else:
          self.head = current.next

        self.length -= 1
        return True

      previous = current
      current = current.next

    raise ValueError('{} is not in list'.format(value))

  # Remove element from list by given index
  def remove_by_index(self, index: int) -> bool:
    self.remove_by_value(self[index])
    return True

  # Get the count of element with given value in list
  def count(self, value: any) -> int:
    count = 0
    current = self.head

    while current:
      if current.value == value:
        count += 1

      current = current.next

    return count

  # Remove all duplicates from linked list
  def remove_duplicates(self) -> None:
    move_count = 0
    # Base case then the list is empty or contains single element
    if not self.head or not self.head.next:
      return

    hashed_elements = set()  # Storage for visited elements
    current = self.head
    hashed_elements.add(current.value)

    # O(n*m)
    while current.next:                             # O(n)
      if current.next.value in hashed_elements:     # O(m)
        temp = current.next
        current.next = current.next.next
        del temp
      else:
        hashed_elements.add(current.next.value)
        current = current.next
      
      move_count += 1



  # Print current list as sorted one
  def print_sorted_list(self) -> None:
    print(list(sorted([int(i) for i in str(self)[1:-1].split(', ')])))


def main() -> None:
  linked_list = LinkedList()

  linked_list + 11
  linked_list + -14
  # linked_list += [15 for _ in range(10)]
  linked_list += [random.randint(-10, 10) for _ in range(100)]

  print('Created linked list:\n', linked_list)
  linked_list.remove_duplicates()
  print('Linked list after removing duplicates:\n', linked_list)


if __name__ == '__main__':
  main()
