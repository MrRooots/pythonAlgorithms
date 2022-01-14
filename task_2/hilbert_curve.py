from turtle import Screen, Turtle


''' 
  Params:
    `step_size`   => length of the each line
    `rotate_by`   => managing the turtle drawing angle | values are -1 or 1
    `curve_level` => current level of the curve
'''
def hilbert_curve(turtle: Turtle, step_size: int, rotate_by: int, curve_level: int) -> None:
  # Stop drawing if cuvre level < 1
  if curve_level < 1:
    return

  turtle.left(rotate_by * 90)   # Rotate
  hilbert_curve(turtle, step_size, - rotate_by, curve_level - 1)
  
  turtle.forward(step_size)     # Move
  turtle.right(rotate_by * 90)  # Rotate
  hilbert_curve(turtle, step_size, rotate_by, curve_level - 1)

  turtle.forward(step_size)     # Rotate
  hilbert_curve(turtle, step_size, rotate_by, curve_level - 1)
  
  turtle.right(rotate_by * 90)  # Rotate
  turtle.forward(step_size)     # Move
  hilbert_curve(turtle, step_size, - rotate_by, curve_level - 1)
  
  turtle.left(rotate_by * 90)   # Rotate


if __name__ == '__main__':
  # Init screen
  screen = Screen()

  # Init turtle
  turtle = Turtle()

  # Set color of the drawing line to black and color of the arrow to green
  turtle.color('black', 'green')
  
  # Set the drawing speed
  turtle.speed(speed=0)

  # Set the brush width
  turtle.width(1.5)

  # Start drawing
  hilbert_curve(turtle=turtle, step_size=10, rotate_by=1, curve_level=4)

  # Drawing until the mouse click
  screen.exitonclick()