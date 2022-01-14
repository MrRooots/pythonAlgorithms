"""
The ternary tree painter
  Python 3.8
  -- Required libraries:
      1) Tkinter (builtin)
      2) turtle (builtin)
      3) math (builtin)

"""

# Imports
from typing import Tuple  # Typing
from turtle import Turtle, Screen  # [Turtle] and [Screen]
import math as math  # [Sin], [cos] and [radians] methods

# Constants
LENGTH = 200  # Length of the initial segment
ANGLE = 120  # Rotation angle always 120 degrees
DEPTH = 3  # Depth of the tree !IMPORTANT: Do not use values more than 10 cause the segment count is more than 100k
segments_count = 0  # Number of segments drawn


# Report printer
def print_report() -> None:
  f_res = sum(3 ** i for i in range(1, DEPTH + 1))

  print('Number of segments required to draw {}-depth ternary tree is: {}'.format(DEPTH, segments_count))
  print()
  print('Formula for segments count of {d}-depth tree is: SUM 3^k for k=1..{d}'.format(d=DEPTH))
  print('Counter result is: {}, formula result is: {} => Formula valid is: {}'.format(segments_count, f_res,
                                                                                      segments_count == f_res))


# Main drawing function
def draw_tree_node(turtle: Turtle, x: float, y: float, length: int, depth: int) -> None:
  if depth < 1:
    return

  # Each level is a tree of three segments from each point of the previous level
  for step in range(3):
    new_angle = math.radians(ANGLE * step)

    turtle.penup()
    turtle.goto(round(x), round(y))

    new_x = round(x + length * math.cos(new_angle))
    new_y = round(y + length * math.sin(new_angle))

    turtle.pendown()
    turtle.goto(new_x, new_y)

    global segments_count
    segments_count += 1

    draw_tree_node(turtle, new_x, new_y, length // 2, depth - 1)


# Initialize [Screen] and [Turtle]
def initialize(instant: bool = False) -> Tuple[Turtle, Screen]:
  # Init screen
  screen = Screen()

  # Set the screen sizes as the monitor capabilities
  screen.setup(width=1.0, height=1.0, startx=None, starty=None)

  # Set window color
  screen.bgcolor('black')

  # Init turtle
  turtle = Turtle()

  # Set color of the drawing line
  turtle.color('yellow')

  # Speed of drawing
  screen.tracer(0, 0) if instant else turtle.speed(1)

  # Set the brush width
  turtle.width(2)

  # Hide turtle
  turtle.hideturtle()

  return turtle, screen


# Controller
def main() -> None:
  # Get initialized [Screen] and [Turtle] instances
  # turtle, screen = initialize()

  # Pass instant=True for instant result
  turtle, screen = initialize(instant=True)

  # Start drawing
  draw_tree_node(turtle, 0, 0, LENGTH, DEPTH)

  # Print drawing report
  print_report()

  # Redraw screen to display the result
  screen.update()

  # Close window on click
  screen.exitonclick()


# Entry point
if __name__ == '__main__':
  main()
