#def average_grade(lst: list) -> dict:
    # Öğrencilerin isimlerini ve notlarını içeren bir liste alacak ve her öğrencinin ortalama notunu dönecek
    # input: [{"isim": "Ali", "not": 80}, {"isim": "Veli", "not": 90}, {"isim": "Ali", "not": 70}]
    # output: {"Ali": 75.0, "Veli": 90.0}

def average_grade(lst: list) -> dict:
    toplam_notlar = {}
    sinav_sayilari = {}

    for ogrenci_verisi in lst:
        isim = ogrenci_verisi["isim"]
        alinan_not = ogrenci_verisi["not"]

        if isim in toplam_notlar:
            toplam_notlar[isim] = toplam_notlar[isim] + alinan_not
            sinav_sayilari[isim] = sinav_sayilari[isim] + 1

        else:
            toplam_notlar[isim] = alinan_not
            sinav_sayilari[isim] = 1

    sonuc_ortalamalar = {}

    for isim in toplam_notlar:
        sonuc_ortalamalar[isim] = toplam_notlar[isim] / sinav_sayilari[isim]

    return sonuc_ortalamalar

ogrenciler_listesi = [
    {"isim": "Ali", "not": 80},
    {"isim": "Veli", "not": 90},
    {"isim": "Ali", "not": 70}
]

sonuc = average_grade(ogrenciler_listesi)

print(sonuc)