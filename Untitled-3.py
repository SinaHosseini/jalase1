first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

score1 = float(input("enter first score "))
score2 = float(input("enter second score "))
score3 = float(input("enter third score "))

average = (score1 + score2 + score3)/3

if average >= 17:
    print("Great", average)

elif 17 > average >= 12:
    print("Normal", average)

else:
    print("Fail", average)
