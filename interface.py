import pygame
import subprocess
import simplejson
import urllib

page = urllib.urlopen("helper.html").read()

pygame.init()

red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
yellow=(255,255,0)
gold=(204,204,0)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Graph theory software')

font=pygame.font.SysFont(None,36)
text1=font.render("Press SPACE to analyze",1,red)
screen.blit(text1,(250,10))
text2=font.render("Press H for help",1,green)
screen.blit(text2,(50,550))

vertex_pos=[]
vertex=[]
edge=[]

n=0
box=[]
All_edge=[]

def vertex_effect(i):
    pos=pygame.mouse.get_pos()
    for member in i:
        if member[0]+3>pos[0]>member[0]-3 and member[1]+3>pos[1]>member[1]-3:
            pygame.draw.circle(screen, gold, [member[0], member[1]], 3, 0)
        else:
            pygame.draw.circle(screen, yellow, [member[0], member[1]], 3, 0)
    pygame.display.update()

def edge_draw(box):
    if len(box)==2:
        All_edge.append(box[:])
        pygame.draw.line(screen, yellow, box[0], box[1], 2)
        pygame.display.update()
        box[:] = []

def v1(i):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
            for member in i:
                if member[0] + 3 > pos[0] > member[0] - 3 and member[1] + 3 > pos[1] > member[1] - 3:
                    box.append(member)

def v2(i):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        for member in i:
                            if member[0] + 3 > pos[0] > member[0] - 3 and member[1] + 3 > pos[1] > member[1] - 3:
                                box.append(member)

def run_Analyze():
    f1 = open('output1.txt', 'w')
    simplejson.dump(vertex_pos, f1)
    f1.close()

    f2 = open('output2.txt', 'w')
    simplejson.dump(All_edge, f2)
    f2.close()

    f3 = open('output3.txt', 'w')
    simplejson.dump(vertex, f3)
    f3.close()

    subprocess.call('analyze.py', shell=True)

def helper():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_h:
            print page

def name_assign():
    i=1
    for member in vertex_pos:
        vertex.append("V"+str(i))
        i+=1

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cur = pygame.mouse.get_pos()
                pygame.draw.circle(screen, yellow, [cur[0], cur[1]], 3, 0)
                vertex_pos.append(cur)
            pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                name_assign()
                run_Analyze()
        vertex_effect(vertex_pos)
        v1(vertex_pos)
        v2(vertex_pos)
        edge_draw(box)
        helper()

pygame.quit()
quit()


#created by Tantatorn Suksangwarn et al.


