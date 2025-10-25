height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in cm: "))

BMI = weight / (height/100)**2
print("Your BMI is ", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healty")
elif BMI <= 29.9:
    print("You are over wieght")
elif BMI <= 34.9:
    print("You are severely over wieght")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")
    