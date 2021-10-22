"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
from time import sleep

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 1

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(50):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(50):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1050, 700]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Initial user position
pos = [0,7]

#Set first grid position to visited
grid[pos[0]][pos[1]] = 1

momentum = 'down'

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and momentum != 'right':
            # Change the x/y screen coordinates to grid coordinates
                momentum = 'left'
            elif event.key == pygame.K_UP and momentum != 'down':
                momentum = 'up'
            elif event.key == pygame.K_RIGHT and momentum != 'left':
                momentum = 'right'
            elif event.key == pygame.K_DOWN and momentum != 'up':
                momentum = 'down'

    if momentum == "left" :
    # Change the x/y screen coordinates to grid coordinates
        pos[1] -= 1
    elif momentum == 'up':
        pos[0] -= 1
    elif momentum == 'right':
        pos[1] += 1
    elif momentum == 'down':
        pos[0] += 1
    #Collision detection
    if pos[0] < 0 or pos[0] > 100:
        pygame.quit()
    elif pos[1] < 0 or pos[1] > 100:
        pygame.quit()
    elif grid[pos[0]][pos[1]] == 1:
        pygame.quit()
    else:
        grid[pos[0]][pos[1]] = 1
    print("Moved to ", pos, "Grid coordinates: ", row, column)
    print("momentum: ",momentum)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(50):
        for column in range(50):
            color = WHITE
            if row == pos[0] and column == pos[1]:
                color = RED
            elif grid[row][column] == 1:
                color = GREEN

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    sleep(0.05)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
