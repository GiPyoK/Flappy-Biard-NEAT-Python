import pygame
import neat
import time
import os
import random

# size of the game screen
WIN_WIDTH = 600
WIN_HEIGHT = 800

# load images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))),
                                    (pygame.image.load(os.path.join("images", "bird2.png"))),
                                    (pygame.image.load(os.path.join("images", "bird3.png")))]
PIPE_IMG = pygame.image.load(os.path.join("images", "pipe.png"))
BASE_IMG = pygame.image.load(os.path.join("images", "pipe.png"))
BG_IMG = pygame.image.load(os.path.join("images", "pipe.png"))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    # top right coner is (0,0)
    def jump(self):
        self.vel = -10.5 # negative value to go up
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        # simultating bird jumping in an arc
        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d >= 16:
            d = 16  # terminal velocity (does not accelerate downward more than 16)
        
        if d < 0 :
            d -= 2

        self.y += d # move the bird in y direction

        # if the bird is moving upward, or higher than the position before jump
        # tilt upward
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else: # tilt downward
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]    
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
        
        # rotate the bird image around the center, not top left 
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)