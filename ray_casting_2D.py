import pygame
import math

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Ray Casting 2D')
clock=pygame.time.Clock()

done=False
m=n=0
x=y=0
x1=y1=0
a=40
x3=[0 for i in range(1000)]
y3=[0 for i in range(1000)]
x4=[0 for i in range(1000)]
y4=[0 for i in range(1000)]
s=[]

for i in range(1000):                       # 1000 light rays (-pi to pi)
    s.append(a)                             # appending slopes of 1000 lines
    if i>=1:
        a=(s[i-1]-math.tan(0.0145))/(1+s[i-1]*math.tan(0.0145))

while not done:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done=True

    screen.fill((0,0,0))
    clock.tick(30)

    m,n=pygame.mouse.get_pos()
    pygame.draw.line(screen,(200,20,20),(200,250),(300,150),2)      # fixed obstacle
    pygame.draw.circle(screen,(250,250,250),(m,n),5)                # light origin mouse

    for j in range(1000):
        x4[j]=((s[j]*m-n+300+150)/(s[j]+1))                         
        y4[j]=(s[j]*(x4[j]-m)+n)                                    # intersection points
        
        if y4[j]>=150 and y4[j]<=250 and x4[j]<=300 and x4[j]>=200:
            if m>=200:
                if m<=300 and m>=200 and (y4[j]<=n and s[j]<0) or (y4[j]>=n and s[j]>=0):
                    pygame.draw.line(screen,(100,100,100),(m,n),((x3[j])+1,(s[j]*(x3[j]-m)+n)))
                else:
                    pygame.draw.line(screen,(100,100,100),(m,n),(round(x4[j])+1,round(s[j]*(x4[j]-m)+n)))
            else:
                pygame.draw.line(screen,(100,100,100),(m,n),((x3[j])+1,(s[j]*(x3[j]-m)+n)))
        else:
            pygame.draw.line(screen,(100,100,100),(m,n),((x3[j])+1,(s[j]*(x3[j]-m)+n)))

    pygame.display.flip()