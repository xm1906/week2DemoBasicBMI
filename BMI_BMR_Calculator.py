# BMI_BMR_Calculator.py
# This program calculates the body mass index and basal metabolic rate

# Calculate BMI
weight = float(input('Enter weight(kg): '))
height = input('Enter height(m): ')

bmi = weight / height

print('BMI: ', bmi)

# Calculate BMR
age = float(input('Enter age(years): '))

bmr =  10 * weight + 6.25 * height - 5 * age + 5

print('BMR: ', bmr)

