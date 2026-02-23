#def pop_dict_zero_values(d: dict) -> dict:
    # Sözlükteki değeri sıfır olan anahtarları pop ile çıkarıp kalan sözlüğü dönecek
    # input: {"a": 1, "b": 0, "c": 3, "d": 0}
    # output: {"a": 1, "c": 3}

def pop_dict_zero_values(d: dict) -> dict:
    silinecekler = []

    for i in d:
        if d[i] == 0:
            silinecekler.append(i)

    for i in silinecekler:
        d.pop(i)

    return d


ornek_sozluk = {"a": 1, "b": 0, "c": 3, "d": 0}
sonuc = pop_dict_zero_values(ornek_sozluk)

print(sonuc)