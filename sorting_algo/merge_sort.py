
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000,700))
screen.fill((255,255,255))
pygame.display.set_caption('Merge Sort Visual')


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
    pygame.time.delay(5)

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


# merge sort algo 

def mergeSort(arr ,l ,r):
    mid = (l+r)//2

    if l <r :
        mergeSort(arr,l,mid)  # left part
        mergeSort(arr,mid+1,r) # right part
        mergeArr(arr,l,mid,mid+1,r)
def mergeArr(arr,x1,y1,x2,y2):
    temp = []
    i= x1 
    j= x2 
    pygame.event.pump()
    while i<=y1 and j<=y2:
        arr_clr[i]= clr[1]
        arr_clr[j]= clr[1]

        fill_window()

        arr_clr[i]= clr[0]
        arr_clr[i]= clr[0]

        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1 
    
    while i<= y1:
        arr_clr[i] = clr[1]
        fill_window()
        arr_clr[i] = clr[0]
        temp.append(arr[i])
        i+=1


    while j<= y2:
        arr_clr[j] = clr[1]
        fill_window()
        arr_clr[j] = clr[0]
        temp.append(arr[j])
        j+=1

    j=0
    for i in range(x1,y2+1):
        pygame.event.pump()
        arr[i] = temp[j]
        j+=1 
        arr_clr[i] = clr[2]
        fill_window()

        if y2-x1 == 148:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]
     

flag = True 

while flag:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            flag= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                new_array()

            if event.key == pygame.K_RETURN:
                mergeSort(arr,0,len(arr)-1)
    fill_window()

            