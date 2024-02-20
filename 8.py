cost = input("Введите кол-во друзей N т кол-во конфет M через пробел: ").split()
if len(cost) == 2:
    candies = int(cost[1]) // int(cost[0])
    bag = int(cost[1]) % int(cost[0])

    print(f"Каждому достанется по {candies} конфеты, в кульке {bag} конфеты")
else:
    print("Ты забыл про конфеты, уходи")