#def is_dict_values_unique(d: dict) -> bool:
    # Bir sözlüğün tüm değerlerinin benzersiz olup olmadığını kontrol edecek
    # input: {"a": 1, "b": 2, "c": 3}
    # output: True
    # input: {"a": 1, "b": 2, "c": 1}
    # output: False

def is_dict_values_unique(d: dict) -> bool:
    gorulen_degerler = []

    for anahtar in d:
        deger = d[anahtar]

        if deger in gorulen_degerler:
            return False

        gorulen_degerler.append(deger)

    return True


ornek_sozluk_1 = {"a": 1, "b": 2, "c": 3}
ornek_sozluk_2 = {"a": 1, "b": 2, "c": 1}

print("1. Sözlüğün Değerleri Benzersiz mi?:", is_dict_values_unique(ornek_sozluk_1))
print("2. Sözlüğün Değerleri Benzersiz mi?:", is_dict_values_unique(ornek_sozluk_2))