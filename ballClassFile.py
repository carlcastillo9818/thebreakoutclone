import pygame
from random import randint

BLACK = (0,0,0)

# ball class inherits from the sprite class
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__() # call the parent class constructor next

        # create var called image which is the surface in this case
        # set surface to be black
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the ball on the surface (a rectangle in this case)
        # surface, color, rectangle_tuple (x,y coords of top left, width, height)
        pygame.draw.rect(self.image, color, [0,0,width,height])

        # create list variable called velocity to hold random vel x and vel y values
        self.velocity  = [randint(4,8), randint(-8,8)]

        # get the rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()

    # update the Ball
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # makes the ball bounce
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)