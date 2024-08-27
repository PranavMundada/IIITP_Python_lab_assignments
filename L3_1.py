dict={}
s=input("Enter a string:")
slen=len(s)
for i in range(slen):
    dict[s[i]]=0
for i in range(slen):
    dict[s[i]]+=1
print(dict)
