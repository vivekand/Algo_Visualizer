import pygame

pygame.init()

screen = pygame.display.set_mode((400, 450))
screen.fill((255, 255, 255))
font = pygame.font.SysFont("comicsans", 20)

grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
vis = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]


def update_display():
    pygame.display.update()


def select_cell(pos, flag):
    j = pos[0] // 50
    i = pos[1] // 50
    if flag == 2:
        grid[i][j] = 2
    elif flag == 3:
        grid[i][j] = 3
    else:
        grid[i][j] = -1
    display_grid()


def display_grid():
    draw_board()
    for i in range(8):
        for j in range(8):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 153, 153), (j * 50 + 5, i * 50 + 5, 45, 45))
            elif grid[i][j] == -1:
                pygame.draw.rect(screen, (0, 0, 0), (j * 50 + 5, i * 50 + 5, 45, 45))
            elif grid[i][j] == 2:
                pygame.draw.rect(screen, (255, 0, 0), (j * 50 + 5, i * 50 + 5, 45, 45))
            elif grid[i][j] == 3:
                pygame.draw.rect(screen, (0, 255, 0), (j * 50 + 5, i * 50 + 5, 45, 45))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (j * 50 + 5, i * 50 + 5, 45, 45))
    update_display()


def reset_grid():
    for i in range(0, 8):
        for j in range(0, 8):
            grid[i][j] = 0
            vis[i][j] = 0


def display_dfs_text():
    text = font.render("Press Enter to start DFS", 1, (0, 0, 0))
    screen.blit(text, (20, 420))
    update_display()


def display_destination_text():
    text = font.render("Select destination", 1, (0, 0, 0))
    screen.blit(text, (20, 420))
    update_display()


def display_source_text():
    text = font.render("Select source", 1, (0, 0, 0))
    screen.blit(text, (20, 420))
    update_display()


def display_obstacle_text():
    text = font.render("Select obstacles", 1, (0, 0, 0))
    screen.blit(text, (20, 420))
    update_display()


def display_error():
    text = font.render("No path between src and dest", 1, (0, 0, 0))
    screen.blit(text, (20, 420))
    update_display()


def display_success_text():
    text = font.render("Success!", 1, (0, 0, 0))
    screen.blit(text, (20, 420))
    update_display()


def draw_board():
    thickness = 5
    for i in range(0, 9):
        pygame.draw.line(screen, (0, 0, 0), (i*50, 0), (i*50, 400), thickness)
        pygame.draw.line(screen, (0, 0, 0), (0, i * 50), (400, i*50), thickness)
    update_display()


def isValid(src):
    if src[0] < 0 or src[0] == 8 or src[1] < 0 or src[1] == 8 or vis[src[0]][src[1]] == 1 or grid[src[0]][src[1]] == -1:
        return False
    return True


def dfs(src, dest):

    if src[0] == dest[0] and src[1] == dest[1]:
        grid[src[0]][src[1]] = 3
        pygame.time.delay(100)
        display_grid()
        return True

    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for move in moves:
        new_x = src[0]+move[0]
        new_y = src[1]+move[1]
        if isValid([new_x , new_y]):
            if grid[new_x][new_y] != 3 or grid[new_x][new_y] != 2:
                grid[new_x][new_y] = 1
            vis[new_x][new_y] = 1
            display_grid()
            pygame.time.delay(100)

            if dfs([new_x , new_y], dest):
                return True
            
            display_grid()

    return False


running = True
draw_board()
display_source_text()
source_selected = False
dest_selected = False
obstacle_selected = False
source = []
des = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not source_selected:
                screen.fill((255, 255, 255))
                draw_board()
                co_ord = pygame.mouse.get_pos()
                select_cell(co_ord, 2)
                source.append(co_ord[1] // 50)
                source.append(co_ord[0] // 50)
                source_selected = True
                display_destination_text()

            elif source_selected and not dest_selected:
                screen.fill((255, 255, 255))
                draw_board()
                co_ord = pygame.mouse.get_pos()
                select_cell(co_ord, 3)
                des.append(co_ord[1] // 50)
                des.append(co_ord[0] // 50)
                dest_selected = True
                display_obstacle_text()

            elif source_selected and dest_selected and not obstacle_selected:
                screen.fill((255, 255, 255))
                draw_board()
                co_ord = pygame.mouse.get_pos()
                select_cell(co_ord, -1)
                display_dfs_text()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if source_selected and dest_selected:
                    if not dfs(source, des):
                        screen.fill((255, 255, 255))
                        draw_board()
                        display_grid()
                        display_error()
                    else:
                        screen.fill((255, 255, 255))
                        draw_board()
                        display_grid()
                        display_success_text()

            if event.key == pygame.K_r:
                reset_grid()
                source_selected = False
                dest_selected = False
                obstacle_selected = False
                screen.fill((255, 255, 255))
                draw_board()
                source = []
                des = []
                display_source_text()