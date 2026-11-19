print("WELCOME TO RIDE BUILDER")
print("Press 1 for car and 2 for bike")
choice=int(input("Enter 1 or 2:"))
if choice==1:
    print("Press 1 for BMW and 2 for Mercedes")
    car=int(input("Enter 1 or 2:"))
    if car==1:
        print("You chose BMW")
    else:
        print("You chose Mercedes")
elif choice==2:
    print("Press 1 for scooty and 2 for mountain bike")
    bike=int(input("Enter 1 or 2:"))
    if bike==1:
        print("You chose scooty")
    else:
        print("You chose mountain bike")
else:
    print("Please put only 1 or 2")