import string

def Sumation(a=0,b=0):
    print("Addition of",a,"and",b,"is: ",a+b) 
def Subtract(a=0,b=0):
    print("Subraction of",a,"and",b,"is: ",a-b)
def Multiply(a=0,b=0):
    print("Multiplication of",a,"and",b,"is: ",a*b)
def Divide(a=0,b=0):
    print("Division of",a,"and",b,"is: ",round(a/b,3))

def ValidateNum(a):
    while(a.isnumeric()):
        return True
    else:
        return False

print("Welcome...")
print("1.Addtion")
print("2.Subtraction")
print("3.Mutiplication")
print("4.Division")

# choice=int(input("please enter the opertion you want: "))

while True :
    choice=input("please enter the opertion you want: ")
    if ValidateNum(choice) :
        choice=int(choice)
        num1=input("Enter the first number: ")
        if ValidateNum(num1):
            num1=float(num1)
            num2=input("Enter the second number: ")
            if ValidateNum(num2):
                num2=float(num2)
                print("Calcutating...")
                break            
            else:
                print("Please enter a value form (1,2,3,4)")
        else:
            print("Please enter a numeric value")
    else:
        print("Please enter a numeric value") 

match choice:
    case 1:
        Sumation(num1,num2)
    case 2:
        Subtract(num1,num2)
    case 3:
        Multiply(num1,num2)
    case 4:
        Divide(num1,num2)
    case _ :
        print("Not a valid choice")

