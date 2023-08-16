import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
def draw_box1(screen, position):
    # Define the size of the box
    box_width = 50
    box_height = 50

    # Draw a white rectangle
    pygame.draw.rect(screen, RED, (position[0], position[1], box_width, box_height))
    
    
def draw_box2(screen, position):
    # Define the size of the box
    box_width = 50
    box_height = 50

    # Draw a white rectangle
    pygame.draw.rect(screen, BLACK, (position[0], position[1], box_width, box_height))

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame.display.set_caption('White Box')
    dt = 0.01
    # Initial position of the box (x, y)
    initial_position1 = [50, 5]
    initial_position2 = [500, 5]
    running = True
    v1 = 5
    v2 = -5
    screen.fill(WHITE)  # Fill the background with black
    draw_box1(screen, initial_position1)
    draw_box2(screen, initial_position2)
    pygame.time.delay(1) 
    time = 0.0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)  # Fill the background with black
        draw_box1(screen, initial_position1)
        draw_box2(screen, initial_position2)            
        time = time +dt
        initial_position1[0] += v1*dt
        initial_position2[0] += v2*dt
        pos1 = initial_position1[0]+ 50
        pos2 = initial_position2[0]
        check = abs(pos1-pos2)
        # check for collision
        if check <=0.1:
            print("yes")
            v1 = -v1
            v2 = -v2
        # check for left wall collision
        checkwall1 = abs(initial_position1[0])
        checkwall2 = abs(550.0-initial_position2[0])
        if checkwall1<=0.01:
            v1 = -v1
            
        if checkwall2<=0.01:
            v2 = -v2
        if time>200:
            break
        draw_box1(screen, initial_position1)
        draw_box2(screen, initial_position2)
        
        
        
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

