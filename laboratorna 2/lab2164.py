height = float(input("Введіть зріст у метрах: "))
weight = float(input("Введіть вагу в кілограмах: "))

bmi = weight / (height * height)

if bmi < 18.5:
    category = "underweight"
elif bmi <= 24.9:
    category = "normal weight"
else:
    category = "overweight"

print(f"Your body mass index is: {bmi:.2f} , that is {category}.")