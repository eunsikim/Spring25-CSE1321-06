import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))

    running = True

    button_img = pygame.image.load("Week-15/Multimedia/assets/button.png")
    button_img = pygame.transform.scale(button_img, (200, 50))

    button_rect = button_img.get_rect()
    button_rect.center = (250, 250)

    myFont = pygame.font.Font(None, 32)
    myFont.set_bold(True)

    text = myFont.render("Click me", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (250, 250)

    beep = pygame.mixer.Sound("Week-15/Multimedia/assets/spawn_sound_1.ogg")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coord = event.pos

                if button_rect.collidepoint(coord[0], coord[1]):
                    beep.play()
                    print("CLICK")

        screen.fill((255, 255, 255))
            
        screen.blit(button_img, button_rect)

        screen.blit(text, text_rect)

        # button_img = pygame.transform.flip(button_img, False, True)
        

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()