from .stack import Stack


class Converter:
  alphabet = None  # Alphabet
  expression_map = None  # Contains the variables definition
  stack = None  # Main stack
  priority = None  # Operators priority values

  # Constructor
  def __init__(self) -> None:
    self.alphabet = (
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    )
    self.expression_map = {}
    self.stack = Stack()
    self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

  #                                       Logic definition

  # Return True if the given operator has less order than the stack top one
  def __get_priority(self, op: str) -> bool:
    return self.priority.get(op, -1) <= self.priority.get(self.stack.peek(), -1)

  # Converts the given expression values into variables
  def __to_variables(self, exp: str) -> str:
    self.expression_map.clear()
    alphabet_index = 0
    result = ''
    i = 0

    while i < len(exp):
      num = ''

      while exp[i] not in ('(', ')', '+', '-', '*', '/', '^'):
        num += exp[i]
        i += 1

        if i == len(exp):
          break

      if num:
        result += self.alphabet[alphabet_index]

        self.expression_map.update({self.alphabet[alphabet_index]: int(num)})
        alphabet_index += 1

      try:
        result += exp[i]
      except IndexError:
        pass

      i += 1

    return result

  # Convert given expression into postfix notation
  def __to_postfix(self, exp: str, hide: bool = False) -> str:
    result = ''
    self.stack.clear()

    for symbol in exp:
      if symbol.isalpha():
        result += symbol

      elif symbol == '(':
        self.stack.add(symbol)

      elif symbol == ')':
        while self.stack.is_not_empty() and self.stack.peek() != '(':
          result += self.stack.pop()
        else:
          self.stack.pop()

      else:
        while self.stack.is_not_empty() and self.__get_priority(symbol):
          result += self.stack.pop()
        self.stack.add(symbol)

    while self.stack.is_not_empty():
      result += self.stack.pop()

    return result

  # Convert given expression into prefix notation
  def __to_prefix(self, exp: str) -> str:
    reversed_exp = ''.join(
      '(' if i == ')' else ')' if i == '(' else i for i in exp[::-1]
    )

    prefix = self.__to_postfix(reversed_exp, hide=True)[::-1]

    return prefix

  #                                           Public methods

  # Convert the given expression variables into saved values
  def to_numbers(self, exp: str, power_replace: bool = False) -> str:
    for variable in self.expression_map.keys():
      exp = exp.replace(variable, str(self.expression_map[variable]))

    return exp if not bool else exp.replace('^', '**')

  # Convert given expression into variables and map then into expression_map
  def to_variables(self, exp: str) -> str:
    if any(i.isdigit() for i in exp):
      exp = self.__to_variables(exp)
      print('[Converter]      | Convert to variables |', exp)
    else:
      print('[Converter]      | Convert to variables | No need')

    return exp

  # Convert given expression into postfix notation
  def to_postfix(self, exp: str) -> str:
    # print('[Converter]      | Working with         |', exp)

    postfix = self.__to_postfix(self.to_variables(exp))

    print('[Converter]      | Convert to postfix   | {}'.format(postfix))

    return postfix

  # Convert given expression into prefix notation
  def to_prefix(self, exp: str) -> str:
    # print('[Converter]      | Working with         |', exp)

    prefix = self.__to_prefix(self.to_variables(exp))

    print('[Converter]      | Convert to prefix    | {}'.format(prefix))

    return prefix
