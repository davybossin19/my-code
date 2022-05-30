
import pygame
from time import sleep

# Define some colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 69, 55)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 1

GRID_ROWS = 50
GRID_COLUMNS = 50

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(GRID_ROWS):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(GRID_COLUMNS):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [555, 555]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Initial user positions
p1_pos = [0,24]
p2_pos = [49,24]

#Set first grid position to visited
grid[p1_pos[0]][p1_pos[1]] = 1
grid[p2_pos[0]][p2_pos[1]] = 2

p1_momentum = 'down'
p2_momentum = 'up'

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and p1_momentum != 'right':
            # Change the x/y screen coordinates to grid coordinates
                p1_momentum = 'left'
            elif event.key == pygame.K_UP and p1_momentum != 'down':
                p1_momentum = 'up'
            elif event.key == pygame.K_RIGHT and p1_momentum != 'left':
                p1_momentum = 'right'
            elif event.key == pygame.K_DOWN and p1_momentum != 'up':
                p1_momentum = 'down'
    
            if event.key == pygame.K_a and p2_momentum != 'right':
            # Change the x/y screen coordinates to grid coordinates
                p2_momentum = 'left'
            elif event.key == pygame.K_w and p2_momentum != 'down':
                p2_momentum = 'up'
            elif event.key == pygame.K_d and p2_momentum != 'left':
                p2_momentum = 'right'
            elif event.key == pygame.K_s and p2_momentum != 'up':
                p2_momentum = 'down'

    if p1_momentum == "left" :
    # Change the x/y screen coordinates to grid coordinates
        p1_pos[1] -= 1
    elif p1_momentum == 'up':
        p1_pos[0] -= 1
    elif p1_momentum == 'right':
        p1_pos[1] += 1
    elif p1_momentum == 'down':
        p1_pos[0] += 1
    
    if p2_momentum == "left" :
    # Change the x/y screen coordinates to grid coordinates
        p2_pos[1] -= 1
    elif p2_momentum == 'up':
        p2_pos[0] -= 1
    elif p2_momentum == 'right':
        p2_pos[1] += 1
    elif p2_momentum == 'down':
        p2_pos[0] += 1
    #Collision detection
    if p1_pos[0] < 0 or p1_pos[0] > GRID_COLUMNS:
        pygame.quit()
    elif p1_pos[1] < 0 or p1_pos[1] > GRID_ROWS:
        pygame.quit()
    elif grid[p1_pos[0]][p1_pos[1]] == 1 or grid[p1_pos[0]][p1_pos[1]] == 2:
        pygame.quit()
    else:
        grid[p1_pos[0]][p1_pos[1]] = 1

    if p2_pos[0] < 0 or p2_pos[0] > GRID_COLUMNS:
        pygame.quit()
    elif p2_pos[1] < 0 or p2_pos[1] > GRID_ROWS:
        pygame.quit()
    elif grid[p2_pos[0]][p2_pos[1]] == 2 or grid[p2_pos[0]][p2_pos[1]] == 1:
        pygame.quit()
    else:
        grid[p2_pos[0]][p2_pos[1]] = 2
    # Set the screen background
    #screen.fill(BLACK)
    print(p1_pos[0], p1_pos[1])
    # Draw the grid
    for row in range(50):
        for column in range(50):
            color = WHITE
            if row == p1_pos[0] and column == p1_pos[1]:
                color = RED
            elif row == p2_pos[0] and column == p2_pos[1]:
                color = BLUE
            elif grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = ORANGE

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
    sleep(0.1)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
