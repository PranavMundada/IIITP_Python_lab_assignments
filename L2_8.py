l1=int(input("Enter the length of 1st side:"))
l2=int(input("Enter the length of 2nd side:"))
l3=int(input("Enter the length of 3rd side:"))

sides=[l1,l2,l3]
sides.sort()

if sides[0]**2+sides[1]**2==sides[2]**2 :
    print("It is Right angled triangle")
else :
    print("It is not a right angled triangle")