import pygame
BLACK = (0,0,0)

# paddle is a child class that inherits from Sprite class
class Paddle(pygame.sprite.Sprite):
    # constructor
    def __init__(self, color, width, height):
        super().__init__() # this calls the parent class constructor

        # pass in color of car and its position
        # set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw paddle
        pygame.draw.rect(self.image, color, [0,0,width,height])

        # get the rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()

    def move_Left(self, pixels):
        self.rect.x -= pixels
        # check screen boundaries
        if(self.rect.x < 0):
            self.rect.x = 0

    def move_Right(self,pixels):
        self.rect.x += pixels

        # check screen boundaries
        if(self.rect.x > 700):
            self.rect.x = 700