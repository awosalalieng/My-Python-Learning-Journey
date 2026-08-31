students=input("Are you a students?(YesNo,): ").lower()
if students=="yes":
    print("Welcom")
    id=input("do you hvae vallid students card?:(Yes,No)").lower()
    if id=="yes":
        print("You can borrow up 5 books")
    else:
        print("Please renew your students card first")
else:
    print("Libraray access is for students only")
