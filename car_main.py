from car import Car

car1 = Car("Mustang", 2024, "Red", False)
car2 = Car("Challenger", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print("")
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print("")
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

print(car1.drive())
print(car2.stop())