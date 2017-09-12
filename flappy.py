import pygame
import math
import random
import os
##from collections import queue


width = 284*2
height = 512


def load_images():

    def load_image(img_file_name):
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background.png'),
            'pipe-end': load_image('pipe_end.png'),
            'pipe-body': load_image('pipe_body.png'),
            'bird-wingup': load_image('bird_wing_up.png'),
            'bird-wingdown': load_image('bird_wing_down.png')}

    
class Queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.remove(0)


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, gravity):
        self.x = x
        self.y = y
        self.gravity = gravity
    def update(self):
        pass
    def collide(self):
        pass

class Pipe:
    def __init__(self, x, gap):
        self.x = x
        self.gap = gap
        self.speed = # some constant here

    def collide(self, )

def main():
    pygame.init()
    pygame.display.set_caption("Flappy Bird by Blahblahboar")
    display = pygame.display.set_mode((width, height))
    images = load_images()
    
    
    while True:
        for x in (0, width/2):
            display.blit(images['background'], (x,0))
        
    pygame.display.flip()

if __name__ == "__main__":
    main()
