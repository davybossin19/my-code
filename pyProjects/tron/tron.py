
import pygame
from player import Player
from time import sleep


# Define some colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (100, 69, 55)
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

P1_KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
P2_KEYS = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
def game_over(screen):
    screen.fill(BLACK)
    fontTitle = pygame.font.SysFont("arial", 50)
    screen.blit(fontTitle.render('GAME OVER!', True, WHITE), (20, 250))
    sleep(10)
    pygame.quit()

def draw_grid(p1, p2, grid, screen):
    for row in range(GRID_ROWS):
            for column in range(GRID_COLUMNS):
                color = WHITE
                if row == p1.y and column == p1.x:
                    color = RED
                elif row == p2.y and column == p2.x:
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


def standby(p1, p2, grid, screen):
    clock = pygame.time.Clock()

    play = False
    while not play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                play = True
        
        draw_grid(p1, p2, grid, screen)

        fontTitle = pygame.font.SysFont("arial", 50)
        screen.blit(fontTitle.render('Press any key to begin!', True, BLACK), (20, 250))    

        clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        sleep(0.1)


def main():
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
    pygame.display.set_caption("Tron")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create Player Instances
    p1 = Player(GRID_COLUMNS // 2, 0, 'down')
    p2 = Player(GRID_COLUMNS // 2, GRID_ROWS - 1, 'up')

    #Set first grid position to visited
    grid[p1.y][p1.x] = 1
    grid[p2.y][p2.x] = 2

    standby(p1, p2, grid, screen)

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN: 
                if event.key in P1_KEYS:
                    p1.set_momentum(event.key)    
                elif event.key in P2_KEYS:
                    p2.set_momentum(event.key)


        # Move position of p1 and p2 based on momentum
        p1.move()
        p2.move()
        
        # Detect Collison, Out of Bounds, and Update Grid 
        if p1.x < 0 or p1.x > GRID_COLUMNS - 1:
            pygame.quit()
        elif p1.y < 0 or p1.y > GRID_ROWS - 1:
            pygame.quit()
        elif grid[p1.y][p1.x] == 1 or grid[p1.y][p1.x] == 2:
            pygame.quit()
        else:
            grid[p1.y][p1.x] = 1

        if p2.x < 0 or p2.x > GRID_COLUMNS - 1:
            pygame.quit()
        elif p2.y < 0 or p2.y > GRID_ROWS - 1:
            pygame.quit()
        elif grid[p2.y][p2.x] == 2 or grid[p2.y][p2.x] == 1:
            pygame.quit()
        else:
            grid[p2.y][p2.x] = 2

        # Draw the grid
        draw_grid(p1, p2, grid, screen)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        sleep(0.1)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
if __name__ == '__main__':
    main()

pygame.quit()
