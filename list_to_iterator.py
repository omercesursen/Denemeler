#def list_to_iterator(lst: list) -> iter:
    # Bir listeyi iterator'a dönüştürecek her çağrıldığında bir sonraki elemanı döndürecek
    # input: [1, 2, 3, 4, 5]
    # output: her çağrıldığında sırayla 1, 2, 3, 4, 5 dönecek

def list_to_iterator(lst: list):
    return iter(lst)


ornek_liste = [1, 2, 3, 4, 5]
iterator_objesi = list_to_iterator(ornek_liste)

print(next(iterator_objesi))
print(next(iterator_objesi))
print(next(iterator_objesi))