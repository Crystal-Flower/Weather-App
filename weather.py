temp=float(input("enter the temperature: "))
is_sunny=eval(input("Enter wether its sunny or not TRUE / FALSE: ")) # --> "True"
if(temp>28 and is_sunny):
    print("the weather is hot")
elif(temp<28 and is_sunny):
    print("the temperature is normal")
elif(temp < 0 and is_sunny):
    print("the temprature is cold")
elif(temp>28 and not is_sunny):
    print("the weather is hot and not sunny")
elif(temp<28 and not is_sunny):
    print("the temperature is normal and not sunny")
elif(temp<0 and not is_sunny):
    print("the temprature is cold and not sunny")
else:
    print("the given value is invalid")
