print("from Celsius to  Fahrenheit enter 1 " )
print("from Fahrenheit to Celsius enter 2 ")
print("____________________________________\n")

choice = int(input("enter what you want to do: "))

match choice:
    case 1:
        celsius=int(input("enter tempreature in Celsius "))
        fahrenheit=(celsius*9/5)+32
        print("the Fahrenheit tempreature is ",fahrenheit)
    
    case 2:
        fahrenheit=float(input("enter tempreature in fahrenheit: "))
        celsius=(fahrenheit-32)*5/9
        print("The Celsius tempreature is ",celsius)

    case _:
        print("you enter wrong number")