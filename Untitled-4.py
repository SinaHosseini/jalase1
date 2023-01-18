weight = float(input("enter your weight(kg)  "))
height = float(input("enter your height(m)  "))

BMI = weight / (height**2)

if BMI <= 18.5:
    print(" Underweight \n", BMI)

elif 18.5 < BMI <= 24.9:
    print(" Normal weight \n", BMI)

elif 25 <= BMI <= 29.9:
    print(" Overweigh \n", BMI)

elif 30 <= BMI <= 34.9:
    print(" Obesity \n", BMI)

elif 35 <= BMI <= 39.9:
    print(" Extreme Obesity", BMI)
