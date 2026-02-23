#def length_of_strings(strings: list) -> dict:
    # Bir liste içindeki her string'in uzunluğunu dönecek
    # input: ["apple", "banana", "cherry"]
    # output: {"apple": 5, "banana": 6, "cherry": 6}

def length_of_strings(strings: list) -> dict:
    uzunluklar = {}

    for kelime in strings:
        uzunluklar[kelime] = len(kelime)

    return uzunluklar


meyveler = ["apple", "banana", "cherry"]
sonuc = length_of_strings(meyveler)

print(sonuc)