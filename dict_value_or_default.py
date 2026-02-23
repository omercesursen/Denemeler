#def dict_value_or_default(d: dict, key, default_value):
    # Bir sözlükte belirli bir anahtarın değerini dönecek, eğer anahtar yoksa varsayılan değeri dönecek
    # input: {"a": 1, "b": 2}, "c", 0
    # output: 0

def dict_value_or_default(d: dict, key, default_value):
    if key in d:
        return d[key]
    else:
        return default_value

ornek_sozluk = {"a": 1, "b": 2}
aranan_anahtar = "c"
varsayilan = 0

sonuc = dict_value_or_default(ornek_sozluk, aranan_anahtar, varsayilan)
print(sonuc)