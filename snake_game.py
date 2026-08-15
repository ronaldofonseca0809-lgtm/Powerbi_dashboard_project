import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 25)


def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def random_food():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return x, y


def game():
    snake = [(100, 100)]
    direction = (CELL_SIZE, 0)

    food = random_food()

    score = 0

    running = True

    while running:

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)

                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)

                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)

                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        new_head = (head_x, head_y)

        # Wall collision
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            running = False

        # Self collision
        if new_head in snake:
            running = False

        snake.insert(0, new_head)

        # Food collision
        if new_head == food:
            score += 1
            food = random_food()
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)

        pygame.draw.rect(
            screen,
            RED,
            (food[0], food[1], CELL_SIZE, CELL_SIZE),
        )

        for segment in snake:
            pygame.draw.rect(
                screen,
                GREEN,
                (segment[0], segment[1], CELL_SIZE, CELL_SIZE),
            )

        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.flip()

    game_over(score)


def game_over(score):

    while True:

        screen.fill(BLACK)

        draw_text("GAME OVER", RED, 220, 130)
        draw_text(f"Score: {score}", WHITE, 240, 180)
        draw_text("Press R to Restart", GREEN, 180, 230)
        draw_text("Press Q to Quit", GREEN, 190, 270)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


game()

