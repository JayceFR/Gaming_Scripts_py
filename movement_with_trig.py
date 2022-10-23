import pygame
import math
screen = pygame.display.set_mode((500,500))

run = True
clock = pygame.time.Clock()
entity_direction = 120
pygame.mouse.set_visible(False)
red_rect = pygame.rect.Rect(100,300,25,25)
click = False
speed = 5
while run:
    clock.tick(60)
    m_pos = pygame.mouse.get_pos()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),m_pos, 5)  
    if click:
        #Getting the 3rd vertex of the triangle
        point = (red_rect.x,m_pos[1])
        #Calculating distance between the points
        l1 = math.sqrt(math.pow((point[1] - red_rect.y), 2) + math.pow((point[0] - red_rect.x), 2))
        l2 = math.sqrt(math.pow((m_pos[1] - point[1]),2) + math.pow((m_pos[0] - point[0]),2))
        #Calculating the angle between them
        angle = math.atan2(l2,l1)
        if l1 < 0:
            angle += math.pi
        angle = math.degrees(angle)
        red_rect.x += math.cos(angle) * speed
        if m_pos[1] < red_rect.y:
            if m_pos[0] < red_rect.x:
                red_rect.y -= math.sin(angle) * speed
            else:
                print(math.sin(angle))
                red_rect.y += math.sin(angle) * speed
        else:
            if m_pos[0] > red_rect.x:
                red_rect.y -= math.sin(angle) * speed
            else:
                print(math.sin(angle))
                red_rect.y += math.sin(angle) * speed

    pygame.draw.rect(screen,(255,0,0),red_rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = not click
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()