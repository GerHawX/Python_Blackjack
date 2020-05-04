class Card:
    def __init__(self, name, nameShort, count):
        self.name = name
        self.nameShort = nameShort
        self.count = count


def createCardDeck():
    cardDeck = []
    categrories = ["Kreuz", "Herz", "Piek", "Karo"]
    values = [("Zwei", 2), ("Drei",3), ("Vier",4), ("Fuenf",5), ("Sechs",6), ("Sieben",7), ("Acht",8), ("Neun",9), ("Bube",10), ("Dame",10), ("Koenig",10), ("Ass",10)]

    for entry in categrories:
        for value in values:
            card = entry + "-" + value[0]
            print (card)

createCardDeck()


