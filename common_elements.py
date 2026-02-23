#def common_elements(lst: list, list2: list) -> list:
    # İki liste arasındaki ortak elemanları dönecek
    # input: [1, 2, 3, 4], [3, 4, 5, 6]
    # output: [3, 4]

def common_elements(lst: list, list2: list) -> list:
    ortak_olanlar = []

    for eleman in lst:
        if eleman in list2:
            ortak_olanlar.append(eleman)

    return ortak_olanlar


liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]

sonuc = common_elements(liste1, liste2)
print(sonuc)