#def is_list_unique(lst: list) -> bool:
    # Bir listenin tüm elemanlarının benzersiz olup olmadığını kontrol edecek
    # input: [1, 2, 3, 4, 5]
    # output: True
    # input: [1, 2, 3, 4, 5, 1]
    # output: False

def is_list_unique(lst: list) -> bool:
    gorulenler = []

    for eleman in lst:
        if eleman in gorulenler:
            return False

        gorulenler.append(eleman)

    return True


ornek_liste_1 = [1, 2, 3, 4, 5]
ornek_liste_2 = [1, 2, 3, 4, 5, 1]

print("1. Liste Benzersiz mi?:", is_list_unique(ornek_liste_1))
print("2. Liste Benzersiz mi?:", is_list_unique(ornek_liste_2))