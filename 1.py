print('Введите общую стоимость:')
cost = float(input("Рубли и копейки указывать через точку!"))
silverWatchMint = 96 * 48
goldWatchNumber = 96 / 16
k = ((cost - silverWatchMint) / goldWatchNumber)
print(f"Здесь у нас только рубли - {int(k)}")
print(f"Здесь у нас рубли и копейки - {k}")