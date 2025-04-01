#import modules
import sys
import pygame

# Manage external resources (currently empty)

# Game classes and functions (currently empty)
def main():
    # Initalize the game
    pygame.init()

    SIZE = width, height = (1024, 768)
    SPEED = [5, 5]
    BLACK = (0, 0, 0)
    FPS = 60

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    
    red_rect = pygame.Rect(0, 0, 50, 50)
    red_surf = pygame.Surface((red_rect.h, red_rect.w))
    red_surf.fill(color=(255, 0, 0))
    

    # Start the main loop
    while True:
        # Listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        
        # Update the game objects as appropriate
        red_rect = red_rect.move(SPEED)

        if red_rect.left < 0 or red_rect.right > width:
            SPEED[0] = -SPEED[0]

        if red_rect.top < 0 or red_rect.bottom > height:
            SPEED[1] = -SPEED[1]
        
        # Update the screen
        screen.fill(BLACK)
        clock.tick(FPS)
        
        # Draw the frame
        screen.blit(red_surf, red_rect)

        # Show the frame
        pygame.display.flip()

if __name__ == "__main__":
    main()