#def value_to_key(d: dict) -> dict:
    # Sözlüğün anahtarları ile değerlerini yer değiştirecek
    # input: {"a": 3, "b": 2, "c": 1}
    # output: {3: "a", 2: "b", 1: "c"}


def value_to_key(d: dict) -> dict:

    ters_sozluk = {}

    for i in d:
        ters_sozluk[d[i]] = i


    return ters_sozluk


ornek_sozluk = {"a": 3, "b": 2, "c": 1}

sonuc = value_to_key(ornek_sozluk)

print(sonuc)