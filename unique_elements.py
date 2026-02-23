#def unique_elements(lst: list, list2: list) -> list:
    # İki liste arasındaki benzersiz elemanları dönecek
    # input: [1, 2, 3, 4], [3, 4, 5, 6]
    # output: [1, 2, 5, 6]

def unique_elements(lst: list, list2: list) -> list:
    benzersizler = []

    for eleman in lst:
        if eleman not in list2:
            benzersizler.append(eleman)

    for eleman in list2:
        if eleman not in lst:
            benzersizler.append(eleman)

    return benzersizler


liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]

sonuc = unique_elements(liste1, liste2)
print(sonuc)