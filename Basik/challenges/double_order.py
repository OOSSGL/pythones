import collections

def _show_ordered():
    inNumbers = (-1, -1, -1, -1, -4, 30, 1, 2, 7, 7, 3, 4, 8, 3, 3, 4, 2, 4, 4, 5, 5, -1, -1, 0, 0)
    ordered = {}

    for n in inNumbers:
        print(n)
        if (n not in ordered):
            ordered[n] = 1
        elif (n in ordered):
            ordered[n] += 1
    # Imprime el dictionario con los datos sin ordenar
    print("Original:", ordered)
    print(type(ordered))

    # Ordena por llave
    ordered2 = sorted(ordered.items())
    print("\nFirst ordering:", ordered2)

    # Ordena por valor
    final_ordered = sorted(ordered2, key=lambda kv: kv[1])
    print("\nFinal:", final_ordered)

    print("\nTest:", sorted(ordered.items(), key = lambda kv:(kv[1], kv[0])))

    for key, value in final_ordered:
        print(key, value, sep=": ")


if __name__ == '__main__':
    _show_ordered()
