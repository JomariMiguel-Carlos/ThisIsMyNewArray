print ("**********      PROGRAMMED BY      **********")
print ("**********  CARLOS, JOMARI MIGUEL  **********")

list = [1, 2, 3, 4, 5, 5, 5, 8, 9, 20]
print("\nArray: ", list)

while True:
    try:
        print("\nMenu:")
        print("1 -> Add an element")
        print("2 -> Insert an element")
        print("3 -> Modify an element")
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

        choice = int(input("\nWhat do you want to do? (1-12): "))
        if choice not in range(1, 14):
            raise ValueError

    except ValueError:
        print("\nInvalid.")

    else:
        if choice == 1:
            try:
                add = int(input("\nEnter the element you want to add: "))
            except ValueError:
                print("\nInvalid.")
            else:
                list.append(add)
                print("\nThis is the new Array: ", list)

        elif choice == 2:
            try:
                insert = int(input("\nEnter the element you want to insert: "))
                insert_ = int(input("\nEnter the index where you want to place: "))
            except ValueError:
                print("\nInvalid.")
            else:
                list.insert(insert_, insert)
                print("\nThis is the new Array: ", list)

        elif choice == 3:
            try:
                modify = int(input("\nEnter the index you want to modify: "))
                modify_ = int(input("\nEnter the element you want to replace: "))
                if modify not in list:
                    raise ValueError
            except ValueError:
                print("\nInvalid.")
            else:
                list[modify] = modify_
                print("\nThis is the new Array: ", list)

        elif choice == 4:
            try:
                delete = int(input("\nEnter the index you want to delete: "))
            except ValueError:
                print("\nInvalid.")
            else:
                list.remove(list[delete])
                print("\nThis is the new Array: ", list)

        elif choice == 5:
            list.sort()
            print("\nThis is the new Array: ", list)

        elif choice == 6:
            list.sort()
            list.reverse()
            print("\nThis is the new Array: ", list)

        elif choice == 7:
            list.pop()
            print("\nThis is the new array:", list)

        elif choice == 8:
            total = sum(list)
            print("\nThis is the sum of all elements:", total)

        elif choice == 9:
            smallest = min(list)
            print("\nThis is the smallest value of element:", smallest)

        elif choice == 10:
            biggest = max(list)
            print("\nThis is the biggest value of element:", biggest)

        elif choice == 11:
            print("\nThere are",len(list),"total number of elements")

        elif choice == 12:
            try:
                count=int(input("\nWhat element you want to count the appearance?"))
                counter=list.count(count)
            except ValueError:
                print("\nInvalid.")
            print("\nThe number of appearance of", count, "is",counter)

        elif choice == 13:
            break