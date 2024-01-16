import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player settings
player_speed = 5
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 2 * player_height

# Bullet settings
bullet_speed = 7
bullet_width, bullet_height = 5, 15
bullets = []

# Enemy settings
enemy_speed = 3
enemy_width, enemy_height = 50, 50
enemies = []

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Blaster")

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Shooting bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y - bullet_height, bullet_width, bullet_height)
        bullets.append(bullet)

    # Move bullets
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    for bullet in bullets:
        bullet.y -= bullet_speed

    # Create enemies
    if random.randint(0, 100) < 3:
        enemy = pygame.Rect(random.randint(0, WIDTH - enemy_width), 0, enemy_width, enemy_height)
        enemies.append(enemy)

    # Move enemies
    enemies = [enemy for enemy in enemies if enemy.y < HEIGHT]
    for enemy in enemies:
        enemy.y += enemy_speed

    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
