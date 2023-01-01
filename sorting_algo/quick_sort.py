
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000,700))
screen.fill((255,255,255))
pygame.display.set_caption('Quick Sort Visual')


width = 1000
height = 600
arr = [0]*150

arr_clr = [(0,204,102)]*150
clr_ind =0
clr= [(143, 40, 158),(0,102,204),(0,255,0),(0,153,153),(223, 143, 235)]

fnt = pygame.font.SysFont('comisson',30)
fnt1 = pygame.font.SysFont('comisson',20)

# generate array  
def new_array():
    for i in range(150):
        arr_clr[i]= clr[0]
        arr[i] = 100*(random.random())

def fill_window():
    screen.fill((255,255,255))
    draw_elements()
    pygame.display.update()
    pygame.time.delay(8)

new_array()

def draw_elements():
    inst1 = fnt.render('Press Enter to start sorting !' ,True ,(80, 199, 88))
    inst2 =  fnt.render('Press R to Reset array Valuse' ,True ,(80, 199, 88))   

    screen.blit(inst1 ,(20,20))
    screen.blit(inst2 ,(20,40))

    element_width = (width- 150)//150
    
    boundry_grp = 550/100
    boundry_arr = 900/150

    pygame.draw.line(screen , (0,0,0) , (0,80) ,(1000,80) ,5)

    for i in range(100):
        pygame.draw.line(screen,(220,220,220) , (0, 85 + i*boundry_grp) ,(1000, 85 + i*boundry_grp))

    for i in range(150):
        pygame.draw.line(screen , arr_clr[i] , (50+boundry_arr*i -3 ,85) , (50+ boundry_arr*i -3 ,85 + boundry_grp*arr[i]) ,5)


# quick sort 

def partition(arr, low, high):
    pygame.event.pump()
    pivot = arr[high]
    arr_clr[high] = clr[2]
    i = low - 1
    for j in range(low, high):
        arr_clr[j] = clr[1]
        fill_window()
        arr_clr[high] = clr[2]
        arr_clr[j] = clr[0]
        arr_clr[i] = clr[0]
        if arr[j] < pivot:
            i = i + 1
            arr_clr[i] = clr[1]
            arr[i], arr[j] = arr[j], arr[i]
    fill_window()
    arr_clr[i] = clr[0]
    arr_clr[high] = clr[0]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1



def quick_sort(arr,st,end):
    if st<end:
        k = partition(arr,st,end)
        quick_sort(arr,st,k-1)

        fill_window()
        for i in range(0,k+1):
            arr_clr[i]= clr[3]

        quick_sort(arr,k+1,end)


flag = True 

while flag:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            flag= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                new_array()

            if event.key == pygame.K_RETURN:
                quick_sort(arr,0,len(arr)-1)
                
    fill_window()

            