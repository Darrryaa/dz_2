# 1. Если страна из нескольких слов
countries = input("Никита введи страну: ")
sliceCountries = countries.split()

for elem in sliceCountries:
    print(elem)

# 2. Если мы вводим страны через запятую
    #countries = input("Никита введи страну: ")
    #sliceCountries = countries.replace(' ', '').split(",") # когда внутри split пусто, мы делим строку по пробелу

    #for elem in sliceCountries:
        #print(elem)
