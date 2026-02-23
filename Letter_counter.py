#def letter_counter(text: str) -> dict:
    # Harflerin sayısını tutacak bir sözlük dönecek
    # input: "aaabbc"
    # output: {"a": 3, "b": 2, "c": 1}

def letter_counter():
    word = input("Metin Giriniz: ")

    dict_1 = {}

    for i in word:
        if i not in dict_1:
            dict_1[i] = 1
        elif i in dict_1:
            dict_1[i] = dict_1[i] + 1

    print(dict_1)


letter_counter()