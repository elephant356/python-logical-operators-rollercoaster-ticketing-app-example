#  else:
#    do that

# (and) A and B = both A & B must be TRUE for the statement to evaluate to TRUE
# (or) A or B = either one can be TRUE or both can be TRUE for the statement to evaluate to TRUE. only when BOTH A and B are FALSE does the statement evaluate to FALSE.
# (not) reverses a statements condition, such as changing a TRUE statement to evaluate as FALSE.
# (not)   for example: a = 12
# (not)                not a > 15 (this evaluates to true, because a = 12 which is NOT greater than 15)

# example code with logical operators (rollercoaster ticket app)

height = int(input("How tall are you in cm? "))
if height < 120:
  print("You are too short to ride the rollercoaster.")

else:
  age = int(input("What is your age in years? "))

bill = 0

if age < 12:
  bill = 5
  print(f"Child tickets are ${bill}")
elif age <= 18:
  bill = 7
  print(f"Youth tickets are ${bill}")
elif age >= 45 and age <= 55:
  bill = 10
  print("You ride for free.")
  
else:
  bill = 12
  print(f"Adult tickets are ${bill}.")

wants_photo = input("Do you want a photo taken Y or N. ")

if wants_photo == "Y":
  bill += 3
  print(f"Your bill is ${bill}.")

else:
  bill = bill
  print(f"Your final bill comes to ${bill}.")
