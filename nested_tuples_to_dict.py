#def nested_tuples_to_dict(nested_tuples: list) -> dict:
    # İç içe geçmiş tuple'ları bir sözlüğe dönüştürecek
    # input: [("a", 1), ("b", 2), ("c", 3)]
    # output: {"a": 1, "b": 2, "c": 3}


def nested_tuples_to_dict(nested_tuples: list) -> dict:
    sonuc_sozlugu = {}

    for i in nested_tuples:
        sonuc_sozlugu[i[0]] = i[1]

    return sonuc_sozlugu


ornek_liste = [("a", 1), ("b", 2), ("c", 3)]
sonuc = nested_tuples_to_dict(ornek_liste)

print(sonuc)