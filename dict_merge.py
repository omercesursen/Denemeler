

def dict_merge(dict_1: dict, dict_2: dict) -> dict:


    dict_3 = {}

    for i in dict_1:
        dict_3[i] = dict_1[i]

    for i in dict_2:
        if i in dict_3:
            dict_3[i] = dict_3[i] + dict_2[i]

        else:
            dict_3[i] = dict_2[i]

    return dict_3



dict_1 = {"a": 1, "b": 2}

dict_2 = {"a": 3, "b": 1, "c": 1}

sonuc = dict_merge(dict_1,dict_2)

print(sonuc)