import pygame
import sys
import json
import os



pygame.init()
pygame.font.init()

if os.path.exists('questions.json'):
    with open('questions.json', 'r') as f:
        data = json.load(f)
else:
    pass

num = 2
currentdict = (list(data.values())[(num - 1)])

data = {}
currentanswer = ''
font = pygame.font.SysFont('Comic Sans MS', 30)
A_text = font.render(currentdict["opA"], True,(255, 255, 255))
B_text = font.render(currentdict["opB"], True,(255, 255, 255))
C_text = font.render(currentdict["opC"], True,(255, 255, 255))
D_text = font.render(currentdict["opD"], True,(255, 255, 255))

print(currentdict["question"], currentdict[currentdict["correct"]])     #for debuging purposes

(width, height) = (1280, 720)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Quiz-it')

class options:
    def __init__(self, width, height, X, Y, color, answer):
        self.width = width
        self.height = height
        self.X = X
        self.Y = Y
        self.color = color
        self.answer = answer
        self.button = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.pressed = False

    def draw(self):
        pygame.draw.rect(window, self.color, self.button)

        status = False
        mousepos = pygame.mouse.get_pos()

        if self.button.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                status = True


        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
            status = False

        return status

opA = options(500, 175, 125, (height - 60 - 175 - 175), (0, 0, 0), currentdict["opA"])
opB = options(500, 175, (width - 500 - 125), (height - 60 - 175 - 175), (0, 0, 0), currentdict["opB"])
opC = options(500, 175, 125, (height - 30 - 175), (0, 0, 0), currentdict["opC"])    #op is short for option
opD = options(500, 175, (width - 500 - 125), (height - 30 - 175), (0, 0, 0), currentdict["opD"])

A_rect = A_text.get_rect(center = opA.button.center)
B_rect = B_text.get_rect(center = opB.button.center)
C_rect = C_text.get_rect(center = opC.button.center)
D_rect = D_text.get_rect(center = opD.button.center)

def panel():
    global width, height
    global currentdict
    global currentanswer
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    answcheck()
                    running = False
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        if opA.draw():
            currentanswer = currentdict["opA"]
        if opB.draw():
            currentanswer = currentdict["opB"]
        if opC.draw():
            currentanswer = currentdict["opC"]
        if opD.draw():
            currentanswer = currentdict["opD"]

        window.fill((255,255,255))
        opA.draw()
        opB.draw()
        opC.draw()
        opD.draw()
        window.blit(A_text, A_rect)
        window.blit(B_text, B_rect)
        window.blit(C_text, C_rect)
        window.blit(D_text, D_rect)
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
