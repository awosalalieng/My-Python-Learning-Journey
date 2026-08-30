total=input("How much is the total pill?:\n")
#convert variable total to float
float_total=(float(total))
#Part 2
tips=input("How much is tips in %:\n")
#converts tips to intger
int_tips=(int(tips))
#Part3
people=input("How many people has already ate?:\n")
#converts people to ins
int_people=(int(people))
tips_amount=((float_total*int_tips)/100)
hole_amount=(tips_amount+float_total)
individual_price=(hole_amount/int_people)
print("Each person pays: " +(str(individual_price)))
