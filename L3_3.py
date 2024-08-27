def gcd(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1

def lcm(num1,num2):
    return abs((num1*num2))//gcd(num1,num2)

n1=int(input("Enter First number:"))
n2=int(input("Enter Second number:"))
print("LCM OF ",n1," and ",n2," is :",lcm(n1,n2))
print("GCD OF ",n1," and ",n2," is :",gcd(n1,n2))