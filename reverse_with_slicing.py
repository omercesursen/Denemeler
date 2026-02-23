#def reverse_with_slicing(lst: list) -> list:
    # Bir listeyi slicing kullanarak tersine çevirecek
    # input: [1, 2, 3, 4, 5]
    # output: [5, 4, 3, 2, 1]


def reverse_with_slicing(lst: list) -> list:
    return lst[::-1]

ornek_liste = [1, 2, 3, 4, 5]
sonuc = reverse_with_slicing(ornek_liste)

print(sonuc)