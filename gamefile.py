# this is a breakout clone game
# import pygame library and initialize game engine
import pygame

# import all other classes
from paddleClassFile import Paddle
from ballClassFile import Ball
from brickClassFile import Brick

pygame.init() # initializes all pygame modules

# color variables
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,176,240)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)


def main():
    game_score = 0  # game score
    game_lives = 3  # number of lives

    # set and open a game window
    window_size = (800, 600)
    window_screen = pygame.display.set_mode(window_size)
    window_title = pygame.display.set_caption("My Breakout Game")

    # a list that contains all the sprites used in the game
    all_sprites_list = pygame.sprite.Group()

    pygame.font.get_fonts()

    # create the paddle for the player
    paddle = Paddle(RED, 100, 10)
    paddle.rect.x = 350
    paddle.rect.y = 550

    # create the ball sprite
    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 300


    all_bricks = pygame.sprite.Group()

    # spawn rows of bricks and add them to the group above
    for x in range(7):
        brick = Brick(BLUE,80,30)
        brick.rect.x = (60 + x * 100)
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for x in range(7):
        brick = Brick(YELLOW, 80, 30)
        brick.rect.x = (60 + x * 100)
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for x in range(7):
        brick = Brick(RED, 80, 30)
        brick.rect.x = (60 + x * 100)
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for x in range(7):
        brick = Brick(ORANGE, 80, 30)
        brick.rect.x = (60 + x * 100)
        brick.rect.y = 180
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for x in range(7):
        brick = Brick(GREEN, 80, 30)
        brick.rect.x = (60 + x * 100)
        brick.rect.y = 220
        all_sprites_list.add(brick)
        all_bricks.add(brick)


    # add the paddle and ball to the list of game sprites
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)


    # bool flag for main game loop
    keepPlaying = True

    # game clock
    game_clock = pygame.time.Clock()

    # main game loop
    while keepPlaying:
        # main event loop
        for event in pygame.event.get():  # indicates user did something
            if (event.type == pygame.QUIT):  # if the user quit the game
                keepPlaying = False  # exit loop
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_x): # press x key to quit
                    keepPlaying = False

        # move paddle when the user presses arrow keys
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            paddle.move_Left(10)
        if(keys[pygame.K_RIGHT]):
            paddle.move_Right(10)

        # game logic goes here
        all_sprites_list.update()

        # check if the ball bounces against any walls
        if(ball.rect.x >= 790):
            ball.velocity[0] = -ball.velocity[0]
        if(ball.rect.x <= 0):
            ball.velocity[0] = -ball.velocity[0]
        if(ball.rect.y > 590):
            ball.velocity[1] = -ball.velocity[1]
            game_lives -=1 # reduce a life when ball hits bottom
            if(game_lives == 0): # display game over
                font = pygame.font.Font(None,80)
                text = font.render("GAME OVER!", 1, WHITE)
                window_screen.blit(text,(250,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                # set keepPlaying to false
                keepPlaying = False

        if(ball.rect.y < 40):
            ball.velocity[1] = -ball.velocity[1]


        # detect collisions between the paddle and the BALL
        if(pygame.sprite.collide_mask(ball, paddle)):
            ball.rect.x -= ball.velocity[0] # change velocities
            ball.rect.y -= ball.velocity[1]
            ball.bounce() # make the ball bounce in opposite direction

        # check for ball and brick collisions
        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

        for brick in brick_collision_list: # CHECK EVERY BRICK
            ball.bounce() # makes the ball bounce away
            game_score += 1 # increase player score
            brick.kill() # makes brick disappear
            if (len(all_bricks) == 0): # display a level complete msg
                font = pygame.font.Font(None,80)
                text = font.render("LEVEL COMPLETE!", 1, WHITE)
                window_screen.blit(text,(200,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                # set keepPlaying to false
                keepPlaying = False


        # drawing stuff goes here
        # make screen blue or any other color
        window_screen.fill(BLACK)

        # line args include surface, color, start pos, end pos, width
        pygame.draw.line(window_screen, WHITE, [0, 45], [800, 45], 4)

        # display the current score and number of lives
        # font args include the font name and the size
        font = pygame.font.Font("convectionui.ttf", 28)
        # text args include the text, antialiasing value, color, and background
        score_text = font.render("Score : " + str(game_score), 1, WHITE)
        # screen arg includes the text you want to see and its position
        window_screen.blit(score_text, (20, 10))
        lives_text = font.render("Player Lives : " + str(game_lives), 1, WHITE)
        window_screen.blit(lives_text, (600, 10))

        # draw all the game sprites after the text is finished
        all_sprites_list.draw(window_screen)

        # update screen here
        pygame.display.flip()

        # limit game to 60 FPS
        game_clock.tick(60)

    # after loop is over, stop the game engine from running
    pygame.quit()
main()

