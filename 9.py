allData = input("Введите кол-во быков N т кол-во семей K через пробел: ").split()
if len(allData) == 2:
    bulls = int(allData[0]) // int(allData[1])
    remains = int(allData[0]) % int(allData[1])
    print(f"Каждому достанется по {bulls} быка, у меня осталось {remains} быка, отпущу их")
else:
    print("В племени нет семей")