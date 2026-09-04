choice = input("Enter membership type (1 for Students or 2 for Teacher): ")
if choice == "1":
    max_books = 3
elif choice == "2":
    max_books = 10
else:
    print("Invalid membership type!")
if choice == "1" or choice == "2":
    books = int(input("How many books do you want to borrow? "))
    
    if books <= max_books:
        print("Borrowing approved!")
    else:
        print("Too many books requested!")
