print ("**********      PROGRAMMED BY      **********")
print ("**********  CARLOS, JOMARI MIGUEL  **********")
print ("**********        BSCOE 2-2        **********")
print ("********** Sir Danilo Madrigalejos **********")

# The list has an initial or original array of 10 random number that consists of
list = [1, 2, 3, 4, 5, 5, 5, 8, 9, 20]
print("\nOriginal array: ", list)

# Display the 13 menu options available
def menu():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("----------------------Menu----------------------\n")
    print("1 -> Add an element")
    print("2 -> Insert an element")
    print("3 -> Modify an index")
    print("4 -> Delete an element")
    print("5 -> Arrange in ascending order")
    print("6 -> Arrange in descending order")
    print("7 -> Remove the last element")
    print("8 -> Sum of all elements")
    print("9 -> Minimum value of an element")
    print("10 -> Maximum value of an element")
    print("11 -> How many elements are there")
    print("12 -> Count the appearance of an element")
    print("13 -> Exit")
    print("Current Array: ", list)

def exit():
    print("Thank you for using this program!")

# If the user choose proper option then
while True:
    menu()
    choice = int(input("\nWhat do you want to do? (1-13): "))

# Option 1 will add an element at the end of the of the list
    if choice == 1:
        app = int(input("\nEnter the element you want to add: "))
        list.append(app)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThe element inserted is:", app)
        print("This is the new Array: ", list)

# Option 2 will insert an element in the chosen index
    elif choice == 2:
        try:
            insert = int(input("\nEnter the element you want to insert: "))
            print("\nThere are", len(list), "index, which is total number of elements, if you exceed \nthe total number of index it will just add at the end of the list")
            index = int(input("\nEnter the index where you want to place: "))
        except ValueError:
            print("\nInvalid.")
        else:
            list.insert(index, insert)
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\nThe element inserted is:",insert)
            print("This is the new Array: ", list)

# Option 3 will edit/modify a value of a chosen index
    elif choice == 3:
        try:
            modify = int(input("\nEnter the index you want to modify: "))
            index = int(input("\nEnter new element you want to place in: "))
            if modify not in list:
                raise ValueError
        except ValueError:
            print("\nInvalid.")
        else:
            list[modify] = index
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\nNew element will be inserted in:", modify)
            print("\nNew element to be inserted is:", index)
            print("This is the new Array: ", list)

# Option 4 will delete the element of the corresponding index
    elif choice == 4:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThere are", len(list), "index, which is total number of elements")
        delete = int(input("\nEnter the index you want to delete(choose between the number of index \nonly or else program will crash: "))
        list.remove(delete)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the new Array: ", list)

# Option 5 will arrange the list in ascending order
    elif choice == 5:
        list.sort()
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the new Array: ", list)

# Option 6 will arrange the list in descending order
    elif choice == 6:
        list.sort()
        list.reverse()
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the new Array: ", list)

# Option 7 will remove the last element of the index
    elif choice == 7:
        list.pop()
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the new array:", list)

# Option 8 will sum up the value of all elements
    elif choice == 8:
        total = sum(list)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the sum of all elements:", total)

# Option 9 will identify the lowest value of element
    elif choice == 9:
        smallest = min(list)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the smallest value of element:", smallest)

# Option 10 will identify the highest value of element
    elif choice == 10:
        biggest = max(list)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThis is the biggest value of element:", biggest)

# Option 11 will count the number of index
    elif choice == 11:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThere are", len(list), "index, which is total number of elements")

# Option 12 will count the appearance of a specific element
    elif choice == 12:
        try:
            count = int(input("\nWhat element you want to count the appearance?: "))
            counter = list.count(count)
        except ValueError:
            print("\nInvalid.")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nThe number of appearance of", count, "is", counter)

# Option 13 will exit/break the program
    elif choice == 13:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("You choose exit option,Bye!")
        exit()
        break

# If the user enter an invalid option it will ask again the user to enter other option
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid Option, Please try again!")

# In every command the program will ask the user if you want to continue
    again = input("\nWould you like to try again the program? type y if yes, if no you can just press enter to end the program: ")
    if again == "y":
        continue
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Thank you for using the program!")
        break