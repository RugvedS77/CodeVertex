import random
import string

def CreatePassword(length,characters):
    password=''.join(random.choice(characters) for _ in range(length)) 
    return password

def Complexity(str):
    if str=='low':
        characters=string.ascii_uppercase + string.digits
    elif str== 'moderate':
        characters=string.ascii_uppercase + string.digits + string.ascii_lowercase
    elif str=='high':
        characters=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    return characters

print("WELCOME...to Password Generator...")
while True:
    passLength=input("Enter length for password: ")
    if passLength.isnumeric():
       passLength=int(passLength)
       if passLength>0 and passLength<=40:
            level=input("Enter the level of complexity of password:\nlow\nmoderate\nhigh\n: ")
            if level =="low" or level=='moderate' or level=='high':
                characters=Complexity(level)
                password=CreatePassword(passLength,characters)
                print("password is: ",password)
                break
            else:
                print("Invalid choice..")
       else:
           print("Please enter a natural number in range of (1-40)")
    else:
        print("Please enter a positive integer..")