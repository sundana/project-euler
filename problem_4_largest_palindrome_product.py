from math import floor


def is_palindrome(n: int) -> bool:
    """Periksa apakah suatu bilangan adalah palindrome.
    Langkah:
        1. Konversi ke string
        2. Bagi string menjadi 2 bagian: kiri dan kanan
        3. Cek apakah bagian kiri sama dengan kebalikan bagian kanan
    """
    n_str = str(n)
    index = floor(len(n_str) / 2)
    if n_str[:index] == n_str[index:][::-1]:
        return True


def largest_palindrome_product(min_val, max_val) -> int:
    """
    Temukan bilangan palindrome terbesar yang merupakan produk dari 2-n digit.
    """
    largest_palindrome = 0
    for i in range(min_val, max_val)[::-1]:
        for j in range(min_val, max_val)[::-1]:
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return (largest_palindrome)


print(largest_palindrome_product(100, 1000))
