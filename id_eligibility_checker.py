is_egyption=input("Are you egyption? (Yes,No): ").lower()
if is_egyption=="yes":
    print("Good")
    is_18=input("Are you 18 or older?  (Yes,no): ").lower()
    if is_18=="yes":
        print("You can issue an id card")
    else:
        print("Sorry you must be 18 or older.")
        print("You can try again when you reach 18.")
else:
    print("sorry this servce only for egyption")
