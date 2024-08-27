str1=input("Enter string 1:")
str2=input("Enter string 2:")
lst1=list(str1)

lst1[0],lst1[1]=lst1[1],lst1[0]
lst2=list(str2)
lst2[0],lst2[1]=lst2[1],lst2[0]
str=''.join(lst1)+" "+''.join(lst2)
print(str)