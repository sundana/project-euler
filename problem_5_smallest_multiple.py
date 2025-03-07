# Brute force
# Cek setiap angka dari nilai minimal hingga maksimal apakah
# bilangan tersebut dapat dibagi tanpa adanya sisa

def smallest_multiple(min_val, max_val):
    score = 0
    smallest = 1
    while score != max_val:
        val = range(min_val, max_val + 1)
        for i in val:
            print("val: ", i)
            if smallest % i == 0:
                score += 1
                print("smallest: ", smallest)
                print("score: ", score)
            else:
                score = 0
                smallest += 1

    return smallest


if __name__ == "__main__":
    min_val, max_val = 1, 20
    result = smallest_multiple(min_val, max_val)
    print(result)
