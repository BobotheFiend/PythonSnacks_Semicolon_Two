#collect weight in kg and height in meters
#calculate the bmi using the formula weight/(height*height)
#print out the bmi status for each class

lbs = int(input("Enter your weight in lbs: "))
inches = int(input("Enter your height in inches: "))

kg = float(0.45359237)*lbs
meters = float(0.0254*inches)
bmi = float(kg/meters*meters)
        
if (bmi< 18.5):
    print(f"Your BMI = {bmi} ---> You are UnderWeight!")

elif (bmi >= 18.5 and bmi <= 24.9):
    print(f"Your BMI = {bmi} ---> You are Healthy!")
        
elif (bmi >= 25.0 and bmi <= 29.9):
    print(f"Your BMI = {bmi} ---> You are OverWeight!")

elif (bmi > 30.0):
    print(f"Your BMI = {bmi} ---> You are Obesed!")
