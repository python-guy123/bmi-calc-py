uw = int(input("Enter your weight in kilograms."))
uh =float(input("Enter your height in meters"))
bmi = uw/(uh**2)
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are in good condition")
elif bmi <30:
    print("you are overweight.")
elif bmi <35:
    print("You are obese")
