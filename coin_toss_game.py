import random
print("Chose a method to toss the coin")
print("1.Using random.randint(0,1)")
print("2.Using random.random()")
choise=input("Enter your choice(1 or 2):")
if choise=="1":
    random_number=random.random()
    if random_number >= 0.5:
        computer_result="Tails"
    else:
        computer_result="Head"
elif choise=="2":
    if random.randint(0,1)==0:
        computer_result="Heads"
    else:
        computer_result="Tails"
else:
    print("Please choose form the list")
choise2=input("Choose one:(Head or Tails:")
if choise2.lower()==computer_result.lower():
    print("congratulation!you won!")
else:
    print("Sorry you lost")
