import pygame

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the player
player_width = 50
player_height = 50
player_x = 50
player_y = screen_height - player_height
player_y_change = 0

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Player jumps
                player_y_change = -10

    # Update player position
    player_y += player_y_change
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height
        player_y_change = 0
    else:
        player_y_change += 1

    # Draw the player and update the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up pygame
pygame.quit()
