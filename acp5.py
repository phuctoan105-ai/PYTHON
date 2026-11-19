age=int(input("How old are you?"))
swim=input("Xan you swim 25 metres ? (yes/no)").lower().strip()
adult=input("Is there an adult with you ? (yes/no)").lower().strip()
print()
print("ENTRY DECISION")
print("-"*32)
if age<4:
    print("Age group : Toddler")
elif age<12:
    print("age group : Child")
elif age<18:
    print("Age group : Teen")
else:
    print("Age group : Adult")

if swim =="yes" and adult=="yes":
    print(" Deep pool: ALLOWED - You can swim and an adult is with you.")
if age<12 and swim=="no":
    print("Shallow end : Stay in the shallw end today")
if not(adult =="yes"):
    print("Reminder - No adult is with you")
if swim !="yes" and swim!="no":
    print("Input error, please check again.")