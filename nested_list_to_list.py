#def nested_list_to_list(nested_list: list) -> list:
    # İç içe geçmiş listeleri tek bir listeye dönüştürecek
    # input: [[1, 2], [3, 4], [5, 6]]
    # output: [1, 2, 3, 4, 5, 6]


def nested_list_to_list(nested_list: list) -> list:
    duz_liste = []

    for alt_liste in nested_list:
        for eleman in alt_liste:
            duz_liste.append(eleman)

    return duz_liste


ornek_liste = [[1, 2], [3, 4], [5, 6]]
sonuc = nested_list_to_list(ornek_liste)

print(sonuc)