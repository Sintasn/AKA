import time

# Faktorial rekursif
def faktorial_rekursif(n):
    if n <= 1:
        return 1
    return n * faktorial_rekursif(n - 1)

# Faktorial iteratif
def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

# Nilai n yang diuji
n_values = [5, 10, 15]

print("+----+----------------------+----------------------+")
print("| n  | Rekursif Time (s)   | Iteratif Time (s)   |")
print("+----+----------------------+----------------------+")

for n in n_values:
    # Waktu rekursif
    start_rec = time.time()
    hasil_rec = faktorial_rekursif(n)
    end_rec = time.time()
    waktu_rec = end_rec - start_rec

    # Waktu iteratif
    start_it = time.time()
    hasil_it = faktorial_iteratif(n)
    end_it = time.time()
    waktu_it = end_it - start_it

    print(f"| {n:<2} | {waktu_rec:<20.8f} | {waktu_it:<20.8f} |")

print("+----+----------------------+----------------------+")