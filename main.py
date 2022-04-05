import pygame
import sys
import json
import os

pygame.init()
pygame.font.init()

data = {}
if os.path.exists('questions.json'):
    with open('questions.json', 'r') as f:
        data = json.load(f)
else:
    pass

num = 1
currentdict = (list(data.values())[(num - 1)])

currentanswer = ''
font = pygame.font.SysFont('Comic Sans MS', 30)
fontsmall = pygame.font.SysFont('Comic Sans MS', 24)
Question_text = font.render(currentdict["question"], True,(255, 255, 255))

print(currentdict["question"], currentdict[currentdict["correct"]])     #for debuging purposes

(width, height) = (1280, 720)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Quiz-it')



class options:
    def __init__(self, width, height, X, Y, answer):
        self.width = width
        self.height = height
        self.X = X
        self.Y = Y
        self.color = (255, 255, 255)
        self.answer = answer
        self.button = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.pressed = False
        self.outline = pygame.Rect(0, 0, self.width + 30, self.height +30)
        self.outline.center = self.button.center
        self.textcolor = (0, 0, 0)
        self.text = font.render(self.answer, True, self.textcolor)
        self.textbox = self.text.get_rect(center = self.button.center)

    def draw(self):
        self.text = font.render(self.answer, True, self.textcolor)
        self.textbox = self.text.get_rect(center=self.button.center)
        pygame.draw.rect(window, (0, 0, 0), self.outline)
        pygame.draw.rect(window, self.color, self.button)
        window.blit(self.text, self.textbox)

        status = False
        mousepos = pygame.mouse.get_pos()

        if self.button.collidepoint(mousepos):
            self.color = (78, 61, 135)
            self.textcolor = (255, 255, 255)
            self.text = font.render(self.answer, True, self.textcolor)
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                status = True
        else:
            self.color = (255, 255, 255)
            self.textcolor = (0, 0, 0)
            self.text = font.render(self.answer, True, self.textcolor)


        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
            status = False

        return status

class button:
    def __init__(self, text, pos):
        self.text = fontsmall.render(text, True, (0, 0, 0))
        self.rect = self.text.get_rect()
        self.pos = pos
        self.pressed = False
    def update(self):
        pos = pygame.mouse.get_pos()
        status = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                status = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
            status = False

        self.rect.center = self.pos
        window.blit(self.text, self.rect)
        return status


opA = options(470, 145, 130, (height - 60 - 175 - 175), currentdict["opA"])
opB = options(470, 145, (width - 470 - 130), (height - 60 - 175 - 175), currentdict["opB"])
opC = options(470, 145, 130, (height - 30 - 175), currentdict["opC"])    #op is short for option
opD = options(470, 145, (width - 470 - 130), (height - 30 - 175), currentdict["opD"])
nextbtn = button('Next', (width - 50, height - 30))


Question_box = pygame.Rect(0, 0, width - 200, 250)
Question_box.center = (width/2, 150)
Question_rect = Question_text.get_rect(center = Question_box.center)
Question_rect.height = (height/2 - 100)


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
            currentanswer = opA.answer
        if opB.draw():
            currentanswer = opB.answer
        if opC.draw():
            currentanswer = opC.answer
        if opD.draw():
            currentanswer = opD.answer

        if nextbtn.update():
            if currentanswer != '':
                answcheck()
                running = False

        window.fill((101, 167, 191))
        opA.draw()
        opB.draw()
        opC.draw()
        opD.draw()
        nextbtn.update()
        pygame.draw.rect(window, (78, 61, 135), Question_box)
        window.blit(Question_text, Question_rect)
        pygame.display.flip()

def update():
    global opA
    global opB
    global opC
    global opD
    global currentdict
    global num
    global Question_text
    global Question_rect
    global currentanswer
    currentanswer = ''
    if num < len(data):
        num +=1
    else:
        num = 1
    currentdict = (list(data.values())[(num - 1)])
    Question_text = font.render(currentdict["question"], True, (255, 255, 255))
    Question_rect = Question_text.get_rect(center=Question_box.center)
    opA.answer = currentdict["opA"]
    opB.answer = currentdict["opB"]
    opC.answer = currentdict["opC"]
    opD.answer = currentdict["opD"]



def answcheck():
    update()
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
