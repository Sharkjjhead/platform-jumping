import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('side-scrolling game')
clock = pygame.time.Clock()
#globals
player = [100, 450, 0, 0]#xpos, ypos, xvel, yvel
isOnGround = False
offset = 0
platforms = [(500, 400), (700, 300)]
########################################################################

def move_player():
    global isOnGround #needed to modify a global variable from within a function
    global offset
    if keys[pygame.K_LEFT]:
        if offset > 260 and player[0]>0:
            player[2] =- 5
        elif player[0]>400 and offset < -1500:
            player[2] =- 5
        elif player[0]>0:
            offset += 4
            player[2] = 0
            
        else:
            player[2]=0
    elif keys[pygame.K_RIGHT]:
        if offset < -1500 and player[0]<750:
            player[2] = 5
        elif offset >260 and player[0]<400:
            player[2] = 5
            
        elif player[0]<750:
            offset -= 4
            player[2] = 0
            
    else:
        player[2] = 0
    
    #if isOnGround == False:
        #player[3] += 1 #gravity
    #else:
        #player[3] = 0
        
    if isOnGround == True and keys[pygame.K_UP]:
      player[3] -= 15 # Player jumps
      isOnGround = False
    
    if isOnGround == False:
        player[3] += 1
        
    player[0]+=player[2] #add x velocity to x positon
    player[1]+=player[3] #add y velocity to y positon
    
    if player [1] > 450:
        isOnGround = True
        player[1] = 450
        player[3] = 0
        
def draw_platforms():
    for i in range(len(platforms)):
        if player[0]+50>platforms[i][0]+offset and player[0]<platforms[i][0]+100+offset and player[1]+50>platforms[i][1] and player[1]+50< platforms[i][1]+50:
            isOnGround = True
            player[1]=platforms[i][1]-50
            player[3] = 0
        
##########################################################################
def draw_clouds():
    for x in range(100, 800, 300):
        for i in range(3):
            pygame.draw.circle(screen, (255,255,255), (x + offset, 100), 40)
            pygame.draw.circle(screen, (255,255,255), (x - 50 + offset, 125), 40)
            pygame.draw.circle(screen, (255,255,255), (x + 50 + offset, 125), 40)
        pygame.draw.rect(screen, (255,255,255), (x - 50 + offset, 100, 100, 65))
def draw_trees():
    for x in range(100, 900, 200):
        for i in range(3):
            pygame.draw.rect(screen, (150,75,0), (x - 10 + offset, 255, 25, 275))
            pygame.draw.circle(screen, (34,139,34), (x + offset, 225), 40)
            pygame.draw.circle(screen, (34,139,34), (x - 50 + offset, 250), 40)
        pygame.draw.circle(screen, (34,139,34), (x + 50 + offset, 250), 40)
def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10), (platforms[i][0] + offset, platforms[i][1], 100, 30))
running = True
while running: # main game loop+++++++++++++++++++++++++++++++++++
    #input section---------------------------------
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    #physics section+++++++++++++++++++++++++++++++++++++++++++++++++
    move_player()
    #platfrom collison
    for i in range(len(platforms)):
        if player[0]+50>platforms[i][0]+offset and player[0]<platforms[i][0]+100+offset and player[1]+50>platforms[i][1] and player[1]+50< platforms[i][1]+50:
            isOnGround = True #stop gravity
            player[1]=platforms[i][1]-50 #reset player's feet
            player[3] = 0 #stop downward velocity
            #print("on platform") #for testing
    # Render section+++++++++++++++++++++++++++++++++++++++++++++++++
    screen.fill((135, 206, 235)) # Sky blue back ground
    draw_clouds() #function call
    draw_trees()
    pygame.draw.rect(screen, (34,139,34), (0, 500 ,800 ,100))
    pygame.draw.rect(screen, (255, 0, 255), (player[0], player[1], 50, 50))
    draw_platforms()
    pygame.display.flip()
    
pygame.display.flip()