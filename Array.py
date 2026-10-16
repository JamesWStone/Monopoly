cars = []

inputCar = str(input("Enter a car brand: "))

with open("cars.txt", "a") as file:
    file.write(inputCar + "\n")

with open("cars.txt", "r") as file:
    for line in file:
        cars.append(line.strip())

print(cars)