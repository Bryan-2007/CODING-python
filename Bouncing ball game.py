import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 149, 221)

# Ball properties
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 4
ball_dy = -4

# Paddle properties
paddle_width = 100
paddle_height = 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 20
paddle_speed = 7

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop variables
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius < 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
        ball_dy = -ball_dy

    # Ball goes below the screen
    if ball_y - ball_radius > HEIGHT:
        print("GAME OVER")
        running = False

    # Drawing everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
