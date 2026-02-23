#def slice_list(lst: list, start: int, end: int) -> list:
    # Bir listeyi verilen başlangıç ve bitiş indekslerine göre dilimleyecek
    # input: [1, 2, 3, 4, 5], 1, 4
    # output: [2, 3, 4]

def slice_list(lst: list, start: int, end: int) -> list:
    return lst[start:end]

ornek_liste = [1, 2, 3, 4, 5]
baslangic = 1
bitis = 4

sonuc = slice_list(ornek_liste, baslangic, bitis)
print(sonuc)