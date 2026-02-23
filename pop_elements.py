#def pop_elements(lst: list, n: int) -> list:
    # Bir listeden n adet elemanı pop yaparak dönecek
    # input: [1, 2, 3, 4, 5], 2
    # output: [1, 2] (liste artık [3, 4, 5] olacak)

def pop_elements(lst: list, n: int) -> list:
    cikan_elemanlar = []

    for i in range(n):
        cikan_elemanlar.append(lst.pop(0))

    return cikan_elemanlar


ornek_liste = [1, 2, 3, 4, 5]
kac_tane = 3

sonuc = pop_elements(ornek_liste, kac_tane)

print("Koparılan Elemanlar (Sonuç):", sonuc)
print("Listenin Kalan Hali:", ornek_liste)