#cmd
#pip install pygame
import pygame
import sys
import random

# 초기화
pygame.init()

# 게임 창 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 30
paddle_speed = 5

# 블록 설정
block_width = 100
block_height = 20
block_x = (screen_width - block_width) // 2
block_y = 50

# 공 설정
ball_radius = 10
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius - 5
ball_dx = 5
ball_dy = -5

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    # 벽과 패들 충돌 처리
    if ball_x <= 0 or ball_x >= screen_width:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_dy = -ball_dy

    # 블록과 공 충돌 처리
    if (
        block_x < ball_x < block_x + block_width
        and block_y < ball_y < block_y + block_height
    ):
        ball_dy = -ball_dy
        block_x, block_y = -100, -100  # 블록을 화면에서 제거

    # 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, RED, (block_x, block_y, block_width, block_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

    # 게임 오버 처리
    if ball_y >= screen_height:
        running = False

# 게임 종료
pygame.quit()
sys.exit()