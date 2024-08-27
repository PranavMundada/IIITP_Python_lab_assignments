str=input("Enter a string :")
l=list(str)
sz=len(str)
l[0],l[sz-1]=l[sz-1],l[0]
newstr=''.join(l)
print("new string is :",newstr)