import pygame
import sys
import json
import os

data = {}

if os.path.exists('questions.json'):
    with open('questions.json', 'r') as f:
        data = json.load(f)

num = 2
currentdict = (list(data.values())[(num - 1)])

print(currentdict["question"], currentdict[currentdict["correct"]])     #for debuging purposes

pygame.init()

(width, height) = (1280, 720)
window = pygame.display.set_mode((width, height))

class options:
    def __init__(self, width, height, X, Y, color, answer):
        self.width = width
        self.height = height
        self.X = X
        self.Y = Y
        self.color = color
        self.answer = answer
        self.button = pygame.Rect(self.X, self.Y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(window, self.color, self.button)


def panel():
    global width, height
    running = True
    opC = options(500, 175, 125, (height - 30 - 175), (0, 0, 0), currentdict["opC"])    #op is short for option
    opD = options(500, 175, (width - 500 - 125), (height - 30 - 175), (0, 0, 0), currentdict["opD"])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    answcheck()
                    running = False
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        window.fill((255,255,255))
        opC.draw()
        opD.draw()
        pygame.display.flip()

def answcheck():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    panel()
                    running = False
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        window.fill((100, 255, 255))
        pygame.display.flip()


panel()
