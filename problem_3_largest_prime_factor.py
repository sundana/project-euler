def largest_prime_factor(n: int) -> int:
    """
    Langkah:
    1. Cari seluruh angka prima yang kurang dari n 
    2. Cari faktor prima dari n
    3. Cari angka prima terakhir
    
    return: largest prime factor of a number
    """
    _temp = 1
    for i in range(2, n): # mulai dari angka 2
        if n % i == 0:
            _temp *= i
            if _temp == n:
                return i
    


sample = 600851475143
# sample = 13195
print(largest_prime_factor(sample))