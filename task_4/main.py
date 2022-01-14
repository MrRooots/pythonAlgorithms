"""
Поддержка: {+, -, *, /} + в выражении не более 26 переменных

Написать  программу,  реализующую  основные  операции  с  бинарными деревьями:
  + построение  дерева  математического  выражения  по  записи  в префиксной форме
  + вывод дерева на экран
  + освобождение памяти, выделенной для дерева

  - Построение дерева математического выражения по записи в инфиксной форме
"""
from task_4.utils.converter import Converter

convert = Converter()


# Execute postfix and prefix converts on given expression
def execute(exp: str) -> None:
  convert.to_postfix(exp)
  print()

  convert.to_prefix(exp)
  print()


def convert_test():
  execute('55+66/14*(21-89)^78^(152)')

  execute('a+b*(c^d-e)^(f+g*h)-i')

  execute('x+y*z/w+u^(k-i)')

  execute('a+b*c-d')


def main():
  exp = '55+(14*40)/14*(21-20)^4^(152-150)+11-2*81^(1/4)'
  print('[Main]      | Computation result   | {} = {}\n'.format(exp, eval(exp.replace('^', '**'))))

  execute(exp)
  print(convert.expression_map)


if __name__ == '__main__':
  main()
