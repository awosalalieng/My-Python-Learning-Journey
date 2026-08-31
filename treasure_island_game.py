#Welcom
print("𝐖𝐞𝐥𝐜𝐨𝐦 𝐭𝐨 𝐦𝐲 𝐢𝐬𝐥𝐚𝐧𝐝")
#input doors for blue you chose the crocodile door game oover!
doors=input("There are two doors in front of you(Blue,Red)").lower()
if doors=="blue":
    print("you chose the crocodile door game oover!")
elif doors=="red":
    print("Great")
    print("Now you enterd a room.")
    boxes=input("you found three booxes:(white,black,Green) ").lower()
    if boxes=="white":
        print(" you opend a box filled with snake")
    elif boxes=="black":
        print("You opend a box filled with spiders")
    elif boxes=="green":
        print("You found the treasure")
    else:
       print("chose sothing in the list")
else:
    print("chose a door from the list")       
