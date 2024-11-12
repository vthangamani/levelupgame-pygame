import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue and Red Sprite Game")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game variables
blue_pos = [200, 200]
blue_width = 20
blue_height = 20
blue_speed = 5
red_pos = [random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)]
red_size = 20
score = 0
game_over = False
win = False

# Font settings
font = pygame.font.Font(None, 36)

# Load background image
background = pygame.image.load("background2.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Win Screen
    if win:
        screen.fill(BLACK)
        win_text = font.render("You Win!", True, WHITE)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        continue

    # Game Over Screen
    if game_over:
        screen.fill(BLACK)
        game_over_text = font.render("Game Over", True, WHITE)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        continue

    # Movement control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_pos[0] -= blue_speed
    if keys[pygame.K_RIGHT]:
        blue_pos[0] += blue_speed
    if keys[pygame.K_UP]:
        blue_pos[1] -= blue_speed
    if keys[pygame.K_DOWN]:
        blue_pos[1] += blue_speed

    # Check for collision with red square
    blue_rect = pygame.Rect(blue_pos[0], blue_pos[1], blue_width, blue_height)
    red_rect = pygame.Rect(red_pos[0], red_pos[1], red_size, red_size)
    if blue_rect.colliderect(red_rect):
        score += 1
        blue_width+= 5  # Increase only the width of blue square
        # Reposition red square
        red_pos = [random.randint(0, WIDTH - red_size), random.randint(0, HEIGHT - red_size)]

    # Check for win condition
    if score >= 10:
        win = True

    # Check if blue square touches edges
    if (blue_pos[0] <= 0 or blue_pos[0] + blue_width >= WIDTH or
            blue_pos[1] <= 0 or blue_pos[1] + blue_height >= HEIGHT):
        game_over = True

    # Draw everything
    screen.blit(background, (0, 0))  # Draw background image
    pygame.draw.rect(screen, BLUE, blue_rect)
    pygame.draw.rect(screen, RED, red_rect)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)  # Set FPS
