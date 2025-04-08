import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))

    r1 = pygame.Rect(0, 0, 200, 200)
    s1 = pygame.Surface((r1.w, r1.h))
    s1.fill((255, 0, 0))

    point1 = (150, 150)
    point2 = (300, 300)
    
    print(r1.collidepoint(point1))
    print(r1.collidepoint(point2))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(color=(0, 0, 0))
        
        screen.blit(s1, (r1.x, r1.y))

        # Draw the coordinate point for point 1
        pygame.draw.circle(screen, (0, 255, 0), (point1[0], point1[1]), 5)
        # Draw the coordinate point for point 2
        pygame.draw.circle(screen, (0, 0, 255), (point2[0], point2[1]), 5)

        pygame.display.flip()


        clock.tick(60)

if __name__ == "__main__":
    main()