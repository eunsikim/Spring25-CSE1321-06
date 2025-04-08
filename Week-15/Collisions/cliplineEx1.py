import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))

    r1 = pygame.Rect(0, 0, 200, 200)
    r1.center = (250, 250)
    s1 = pygame.Surface((r1.w, r1.h))
    s1.fill((255, 0, 0))

    line1 = ((50, 400), (450, 100))
    line2 = r1.clipline(line1)

    print(line2)
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(color=(0, 0, 0))
        
        screen.blit(s1, (r1.x, r1.y))

        pygame.draw.line(screen, (255, 255, 255), line1[0], line1[1], width=3)
        pygame.draw.line(screen, (0, 0, 255), line2[0], line2[1], width=3)

        pygame.display.flip()


        clock.tick(60)

if __name__ == "__main__":
    main()