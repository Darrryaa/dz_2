# 1кг - 0.453592
# 1см - 0,39
pounds = float(input("Введите вес в фунтах: "))
inches = float(input("Введите высоту в дюймах: "))
poundsKG = pounds * 0.453592
inchesM = inches * 0.39 / 100

indexWeight = poundsKG / inchesM ** 2
print(f"Индекс массы тела: {indexWeight:.2f}")