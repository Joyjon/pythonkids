# imports, globals and drawing
import pygame
import random
import time

# initialize pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 127, 0)
blue = (0, 0, 255)
brown = (128, 64, 0)
violet = (127, 0, 255)
tennis_green = (169, 218, 30)
grey = (127, 127, 127)
grey_blue = (76,141,174)


# screen globals
screen_width = 1472
screen_height = 828

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Welcome To Tiny Tennis!!!!!!!!!!!!!!!")
font = pygame.font.SysFont("monospace", 75)

# ball globals
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
ball_xv = 10
ball_yv = 10
ball_r = 20

# draw paddle 1
paddle1_x = 10
paddle1_y = 10
paddle1_w = 15
paddle1_h = 100

# draw paddle 2
paddle2_x = screen_width - 35
paddle2_y = 10
paddle2_w = 15
paddle2_h = 100


# initialize score
player1_score = 0
player2_score = 0

# moving the paddles
# game loop
pygame.mouse.set_visible(0)
do_main = True
serve_start = False
while do_main:
    pressed = pygame.key.get_pressed()
    pygame.key.set_repeat()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do_main = False
    if pressed[pygame.K_ESCAPE]:
        do_main = False

    if pressed[pygame.K_w]:
        paddle1_y -= 15
    elif pressed[pygame.K_s]:
        paddle1_y += 15

    if pressed[pygame.K_UP]:
        paddle2_y -= 15
    elif pressed[pygame.K_DOWN]:
        paddle2_y += 15

    if pressed[pygame.K_SPACE]:
        serve_start = True

# the serving

    if serve_start == True:
        ball_x += ball_xv
        ball_y += ball_yv

# collision of ball with top/bottom of screen
    if ball_y - ball_r <= 0 or ball_y + ball_r >= screen_height:
        ball_yv *= -1

# collision of paddle with top/bottom of screen
    if paddle1_y < 0:
        paddle1_y = 0

    elif paddle1_y + paddle1_h > screen_height:
        paddle1_y = screen_height - paddle1_h

    if paddle2_y < 0:
        paddle2_y = 0

    elif paddle2_y + paddle2_h > screen_height:
        paddle2_y = screen_height - paddle2_h

# left paddle
    if ball_x - ball_r - 10 < paddle1_x + paddle1_w  and ball_y >= paddle1_y and ball_y<= paddle1_y + paddle1_h:
        ball_xv *= -1


# right paddle
    if ball_x + ball_r > paddle2_x -10 and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle2_h:
        ball_xv *= -1


# keeping score
    if ball_x - ball_r <= 0:
        player2_score += 1
        serve_start = False
# serving position?
        ball_x = int(paddle2_x - ball_r)
        ball_y = int(paddle2_y + paddle2_h / 2)

    elif ball_x + ball_r >= screen_width:
        player1_score += 1
        serve_start = False
# serving position?
        ball_x = int(paddle1_x + paddle1_w + ball_r)
        ball_y = int(paddle1_y + paddle1_h / 2)

# rendering screen
    game_screen.fill(grey_blue)
    paddle_1 = pygame.draw.rect(game_screen, red, (paddle1_x, paddle1_y, paddle1_w, paddle1_h), 0)
    paddle_2 = pygame.draw.rect(game_screen, blue, (paddle2_x, paddle2_y, paddle2_w, paddle2_h), 0)
    net = pygame.draw.line(game_screen, white, (736,8), (736,820))
    ball = pygame.draw.circle(game_screen, tennis_green, (ball_x, ball_y), ball_r, 0)

# displaying scores
    score_text = font.render("P1" + ": " + str(player1_score) + "    " + "P2" + ": " + str(player2_score), 1, white)
    game_screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))



    # displaying the game winner
    if player1_score >= 10:
        # print("Player1 ,you win!")
        ball_xv = 0
        ball_yv = 0
        win_test1 = font.render("Player1, YOU WIN!!!", 1, red)
        game_screen.blit(win_test1, (screen_width / 2 - win_test1.get_width() / 2, 100))

    elif player2_score >= 10:
        # print("Player2 ,you win!")
        ball_xv = 0
        ball_yv = 0
        win_test2 = font.render("Player2, YOU WIN!!!", 1, blue)
        game_screen.blit(win_test2, (screen_width / 2 - win_test2.get_width() / 2, 100))

    pygame.display.update()

    time.sleep(0.016666667)
# ending the game
pygame.quit()