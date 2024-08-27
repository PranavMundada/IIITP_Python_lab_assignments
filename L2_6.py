num=int(input("Enter 1 to convert celcius into fahrenheit ./n Enter 2 to convert from fahrenheit to celcius"))

if num==2 :
    temp=(int(input("Enter the temperature in fahrenheit:")))
    print(5*((temp-32)/9),"is temperature in celcius.")
else :
    temp=(int(input("Enter the temperature in fahrenheit:")))
    print((9*temp)/5+32,"is temperature in celcius.")