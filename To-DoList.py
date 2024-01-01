
def CreateList():
    while True:
        Item1=input("Enter the item you wish to add: ")
        # if Item1.isalpha() or Item1.isspace():
        if any(char.isalpha() for char in Item1) or ' ' in Item1:
            print("Added successfully")
            return Item1
        else:
            print("Please enter a sentence")

def Check(str1,lst):
    return str1 in lst
       
def UpdateList():
    print("1.Change existing entry")
    print("2.Delete an entry")
    ChoiceList=['1','2']

    while True:
        choice2 = input("Please Enter the choice: ")
        if choice2 in ChoiceList:
            choice2=int(choice2)
            match choice2:
                case 1:
                    Oldentry=input("Enter the entry to be changed: ")
                    if Check(Oldentry,MyList) :
                        EntryIndex=MyList.index(Oldentry)
                        NewEntry=input("Enter new entry: ")
                        MyList[EntryIndex]=NewEntry
                        print("Updated Successfully...")
                        break
                    else:
                        print("Item not found in list")

                case 2:
                    Oldentry=input("Enter the entry to be deleted: ")
                    if Check(Oldentry,MyList) :
                        MyList.remove(Oldentry)
                        print("Deleted Successfully")
                        break
                    else:
                        print("Item not found in list")

def TrackList(lst):
    print("Your current To-Do List: ")
    i=1
    for item in lst:
        print(i,". ",item)
        i+=1

def SaveToFile(MyList):
    with open('ToDoList.txt','w') as file:
        file.write('\n'.join(MyList))

def LoadFromFile():
    try:
        with open('ToDoList.txt','r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found. Creating a new list.")
        return []

MyList=LoadFromFile()

ChoiceList=['1','2','3','4']
Exit=False

print("Welcome to your To-Do list...")
while not Exit:
    print("1.Create a list")
    print("2.Update the list")
    print("3.Track the list")
    print('4.Save and Exit')

    while True:
        choice = input('enter your choice: ')
        if choice in ChoiceList:
            choice=int(choice)
            match choice:
                case 1:
                    a=CreateList()
                    MyList.append(a)
                case 2:
                    UpdateList()
                case 3:
                    TrackList(MyList)
                case 4:
                    print("Saving list to file and exiting...")
                    SaveToFile(MyList)
                    Exit=True
                    break
                case _:
                    print("Not a correct choice...please re-enter your choice")
        else:
            print("Enter a valid choice...")                  