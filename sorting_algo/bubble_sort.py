import random
import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))
screen.fill((255,255,255))
pygame.display.set_caption('Bubble sort Visual')

arr = []
width = 20
x= 40
y= 40
# generating a randon array with length 20
def ResetArr():
    for i in range(20):
        x= 200*(random.random() + 0.2)
        arr.append(x)
# updating display with suitable bar
def updateDisplay():
    pygame.display.update()
# showing array with rectangular bar
def ShowArr():
    for i in range(20):
        pygame.draw.rect(screen , (60,60,60) , (x+ 30*i ,y , width , arr[i]))
    updateDisplay()
# fornt used
font = pygame.font.SysFont('comisson',25)

def start_instruction():
    text = font.render('Please Press Enter to start !' , True ,(80, 199, 88))
    screen.blit(text ,(100,500))
    updateDisplay()

def Reset_instruction():
    text = font.render('Please Press R to reset the array values!' , True ,(80,199,88))
    screen.blit(text ,(100,550))
    updateDisplay()


def Bubble_sort():
    for i in range(19,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            screen.fill((255,255,255))
            ShowArr()
            pygame.time.wait(50)


flag = True 

ResetArr()
ShowArr()
start_instruction()
Reset_instruction()
updateDisplay()

while flag:
    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Bubble_sort()
                
            elif event.key == pygame.K_r:
                arr.clear()
                screen.fill((255,255,255))
                ResetArr()
                ShowArr()
                start_instruction()
                Reset_instruction()