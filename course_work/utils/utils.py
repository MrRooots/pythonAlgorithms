import os


class MyUtils:
  @staticmethod
  def clear_console():
    os.system('cls')

  @staticmethod
  def print_desk(desk: list, iteration: int, width: int):
    print(' ' * 15, '{} Iteration'.format(iteration))
    index = 0
    is_first = True
    i = 4

    for row in desk:
      strings_by_column = [s.split('\n  ') for s in row]
      strings_by_line = zip(*strings_by_column)

      for parts in strings_by_line:
        if parts[0] not in ('', '  '):
          a = [i for i in parts]
          index += 1

          if is_first and index % 3 == 0:
            a.insert(0, str(i))
            a.append(' <-- Black side')
            index = 0
            i -= 1
            is_first = False
          elif index % 5 == 0:
            a.insert(0, str(i))
            index = 0
            i -= 1
          else:
            a.insert(0, ' ')

          print(''.join(a))

    print(
      '      0' + ''.join(['         ' + str(i) for i in range(1, width)])
    )
