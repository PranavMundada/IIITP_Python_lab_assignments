m1=int(input("Enter the marks of test 1:"))
m2=int(input("Enter the marks of test 2:"))
m3=int(input("Enter the marks of test 3:"))

marks=[m1,m2,m3]
marks.sort()

print("Average of best 2 test marks out of 3:",(marks[1]+marks[2])/2)