import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")

running = True
game_over = False
paused = False

snake_x = 100
snake_y = 100

direction_x = 0
direction_y = 0

food_x = random.randrange(0, 580, 5)
food_y = random.randrange(0, 380, 5)

score = 0
speed = 10

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 70)
score_text=pygame.font.Font(None,56)
snake_length = 1
snake_body = []

clock = pygame.time.Clock()

while running:

    screen.fill((25, 25, 25))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                paused = not paused

            if not paused and not game_over:

                if event.key == pygame.K_RIGHT:
                    direction_x = 5
                    direction_y = 0

                if event.key == pygame.K_LEFT:
                    direction_x = -5
                    direction_y = 0

                if event.key == pygame.K_UP:
                    direction_x = 0
                    direction_y = -5

                if event.key == pygame.K_DOWN:
                    direction_x = 0
                    direction_y = 5

    if not paused and not game_over:

        snake_x += direction_x
        snake_y += direction_y

        snake_body.append((snake_x, snake_y))

        if len(snake_body) > snake_length:
            snake_body.pop(0)

        if snake_x < 0 or snake_x > 580:
            game_over = True

        if snake_y < 0 or snake_y > 380:
            game_over = True

        if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:

            food_x = random.randrange(0, 580, 5)
            food_y = random.randrange(0, 380, 5)

            score += 1
            snake_length += 1

            if speed < 30:
                speed += 1

    for segment in snake_body:
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (segment[0], segment[1], 20, 20)
        )

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (food_x, food_y, 20, 20)
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    if paused:
        pause_text = font.render(
            "PAUSED",
            True,
            (255, 255, 0)
        )
        screen.blit(pause_text, (240, 180))

    if game_over:
        game_over_text = game_over_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )
        screen.blit(game_over_text, (110, 160))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()

