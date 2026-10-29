field1=105
field2=97
field3=123
field4=118
field5=95

total= field1 + field2 + field3 + field4 + field5
average= total/5

print("The total is:",total,"kg")
print("The average is:",average,"kg")

price=20
earnings=total*price
print("The total earnings is at:",earnings)

bags= total // 25
leftover = total % 25
print("The total number of bags is:",bags)
print("The leftover grains are at:",leftover)
print("\n")

last_year = 500
print("Better than last year:",total>last_year)
print("Same as last year:",total==last_year)
print("At least as good:",total>=last_year)
print("\n")

total += 30
print("After this bonus:",total,"kg")

total-= 15
print("After seed reserve:",total,"kg")

bags= total // 25
print("The final bags:",bags)