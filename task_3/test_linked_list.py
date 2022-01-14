import random as random
from task_3.linked_list import LinkedList


def test():
  linked_list = LinkedList()

  assert linked_list.length == 0, 'Invalid list length after initialization'

  length = random.randint(0, 1001)
  elements = [round(random.uniform(-100, 100), 2) for _ in range(length)]

  linked_list + elements

  assert linked_list.length == length, 'Invalid list length after adding elements'
  print('Length result: passed!')

  assert str(linked_list) == '[' + ', '.join(str(i) for i in elements) + ']', 'Invalid list values after adding'
  print('Print values:  passed!')


if __name__ == '__main__':
  test()
