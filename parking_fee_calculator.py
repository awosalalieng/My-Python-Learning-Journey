parking_car=float(input("How many hours you want to park? :\n"))
if parking_car <= 2:
    print(f"You spend {parking_car} Hours Total fee: it's free")
elif parking_car <=5:
    extra_hours=parking_car-2
    fee=extra_hours*5
    print(f"You spend {parking_car} Total fee: {fee} Ringgit ")
elif parking_car <=10:
    print(f"You spend {parking_car} Total fee: 20 Ringgit ")
else:
    extra_hours2=parking_car-10
    extra_fee=extra_hours2*3
    total=35+extra_fee
    print(f"You spend {parking_car} Total fee: {total}")
