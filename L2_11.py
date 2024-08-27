sent = input("Enter a sentence : ")


wordCount = len(sent.split())
print("Number of words in this sentence are : ",wordCount)
upper, lower, number = 0, 0, 0
for i in range(len(sent)):
       if sent[i].isupper():
           upper += 1
       elif sent[i].islower():
           lower += 1
       elif sent[i].isdigit():
           number += 1


print("Number of digits in this sentence are : ",number)
print("Number of uppercase letters : ",upper)
print("Number of lowercase letters :",lower)