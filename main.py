import pygame
import player

win_dim = (800, 600)
fs = False  # Fullscreen
win = pygame.display.set_mode(win_dim, pygame.RESIZABLE | pygame.SCALED)
done = False

while not done:
    # Update
    win_dim = pygame.display.get_window_size()

    # Input
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    elif event.type == pygame.QUIT:
        done = True

    # Draw
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 0), (80, 300, 50, 50))
    pygame.display.flip()

pygame.quit()