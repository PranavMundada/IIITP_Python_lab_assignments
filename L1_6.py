from decimal import Decimal
a=0.1+0.2
if a!=0.3:
    print("0.1+0.2 is not equal to 0.3")
b=Decimal('0.1')+Decimal('0.2')
print("Using decimal module we get the correct ans: ",b)