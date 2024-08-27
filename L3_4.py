def ball_collide():
    print("Enter the coordinates and radius of ball 1: ")
    x1=int(input())
    y1=int(input())
    r1=int(input())
    print("Enter the coordinates and radius of ball 1: ")
    x2=int(input())
    y2=int(input())
    r2=int(input())
    b1=(x1,y1,r1)
    b2=(x2,y2,r2)
    if (b1[0]-b2[0])**2+(b1[1]-b2[1])**2<=(b1[2]+b2[2])**2 :
        return 1
    else :
        return 0

x=ball_collide()
if x:
    print("Balls collide.")
else :
    print("Balls do not collide.")

