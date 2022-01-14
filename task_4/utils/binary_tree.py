"""
Ограничения:
  - Поддерживаются только {+, -, *, /, ^}
  - В выражении не более 26 переменных, так как каждое число будет заменено на букву английского алфавита
    - Пример: 120+152/42^2 --> A+B/C^D

Написать  программу,  реализующую  основные  операции  с  бинарными деревьями:
  + Построение  дерева  математического  выражения  по  записи  в префиксной форме <----
  + Вывод дерева на экран --> Вывод инфиксного выражения                                |
  + Освобождение памяти, выделенной для дерева                                          |
                                                                                        |
  + Построение дерева математического выражения по записи в инфиксной форме             |
    - Реализовано через конвертацию инфикса в префикс 0_о   ----------------------------
"""

from task_4.utils.converter import Converter


# Tree node implementation
class TreeNode:
  data = None  # Data
  left = None  # Left node
  right = None  # Right node

  def __init__(self, data):
    self.data = data


# Expression tree implementation
class ExpressionTree:
  head = None  # Head of the current tree
  priority = None  # Priority list of operators
  output = None  # Output expression
  convert = None  # Converter instance

  def __init__(self) -> None:
    self.head = None
    self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    self.output = ''
    self.convert = Converter()

  # Return True if the given operator has less order than the stack top one
  def __get_priority(self, op: str, op2: str) -> bool:
    return self.priority.get(op, 0) <= self.priority.get(op2, 0)

  # Display the tree as expression
  def __display(self, node: TreeNode = None) -> None:
    node = self.head if node is None else node
    if node.left and node.right:
      if self.__get_priority(node.left.data, node.right.data):
        self.output += '('

      self.__display(node.left)
      self.output += node.data
      self.__display(node.right)

      if self.__get_priority(node.left.data, node.right.data):
        self.output += ')'

    else:
      self.output += node.data

  # Build tree from the given prefix expression
  def from_prefix(self, exp: str) -> None:
    self.head = self.add(exp)[0]

  # Build tree from given infix expression
  def from_infix(self, exp: str) -> None:
    self.from_prefix(self.convert.to_prefix(exp))

  # Add node
  def add(self, exp_part: str):
    if exp_part[0].isalpha():
      return TreeNode(exp_part[0]), exp_part[1:]
    else:
      node = TreeNode(exp_part[0])
      node.left, part = self.add(exp_part[1:])
      node.right, part = self.add(part)

      return node, part

  def print_tree(self, node, level=0):
    if node:
      print(' '*level + node.data)

      level += 1
      self.print_tree(node.left, level)
      self.print_tree(node.right, level)

  # Convert expression tree into infix notation
  def to_infix(self, node: TreeNode) -> str:
    if node.left and node.right:
      if self.__get_priority(node.left.data, node.right.data):
        self.output += '('

      self.to_infix(node.left)

      self.output += node.data

      self.to_infix(node.right)

      if self.__get_priority(node.left.data, node.right.data):
        self.output += ')'

    else:
      self.output += node.data

    return self.output

  # Display whole tree as infix expression
  def display(self) -> None:
    self.__display()

    print('[ExpressionTree] | Expression from tree | {}'.format(self.output))
    self.output = ''

  # Evaluate the tree expression
  def evaluate(self, exp: str = None) -> float:
    return eval(self.convert.to_numbers(self.output if not exp else exp, power_replace=True))


# Driver code
def main() -> None:
  tree = ExpressionTree()
  expression = '55+(14*40)/14*(21-20)^4^(152-150)+11-2*81^(1/4)'
  expression = '***abcd'

  # print('[Main]           | Expression result    |', tree.evaluate(exp=expression))

  # print('\n--------------------------------- Tree from infix expression ---------------------------------')
  # print('[Main]           | Initial expression   |', expression)
  #
  # tree.from_infix(expression)
  # # tree.display()
  #
  # expression = '+A+/*BC*D^-EF^G-HI-J*K^L/MN'
  # print('\n--------------------------------- Tree from prefix expression ---------------------------------')
  # print('[Main]           | Initial expression   |', expression)

  tree.from_prefix(expression)
  tree.print_tree(tree.head)
  tree.display()


# Entry point
if __name__ == '__main__':
  main()
