rama=input("Enter the birthdate: ")
shyam=input("Enter the birthdate: ")
components1=rama.split("-")
components2=shyam.split("-")



Rama={
"Year":components1[2],
"Month":components1[1],
"Date" :components1[0]
}
Shyam={
"Year":components2[2],
"Month":components2[1],
"Date" :components2[0]
}

print("Rama is born on ",rama," shyam is born on ",shyam)
print("Rama turns ",2024-int(Rama["Year"])," years on the date",Rama["Date"],Rama["Month"],2024)
print("Shyam turns ",2024-int(Shyam["Year"])," years on the date",Shyam["Date"],Shyam["Month"],2024)