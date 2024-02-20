def lab_4():
    riddle = "Когда мы шли с человеком и его семью женами в Сент-Айвс. Каждая жена имела по семь мешков, каждом мешке - по семь кошек, а у каждой кошки было семь котят. Котята, кошки, жены… Сколько всего шло в Сент-Айвс?"

    someText1 = "мы"
    someText2 = "семью женами"
    someText3 = "семь мешков"
    someText4 = "семь кошек"
    someText5 = "семь котят"

    numRunner = 0

    if someText1 in riddle:
        numRunner += 2

    if someText2 in riddle:
        numWife = 7
        numRunner += numWife
    else:
        numWife = 0
        print(numRunner)
        return

    if someText3 in riddle:
        numBags = numWife * 7
        numRunner += numBags
    else:
        numBags = 0
        print(numRunner)
        return

    if someText4 in riddle:
        numCats = numBags * 7
        numRunner += numCats
    else:
        numCats = 0
        print(numRunner)
        return

    if someText5 in riddle:
        numLitleCats = numCats * 7
        numRunner += numLitleCats
    else:
        print(numRunner)
        return

    print(f"Всего человек: {numRunner}")

def main():
    lab_4()

if __name__ == "__main__":
    main()
