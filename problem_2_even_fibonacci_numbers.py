def even_fibonacci_numbers() -> int:
    """
    return: the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million
    """
    max_value = 3_524_578
    fib_list = [1, 2]
    result = []
    while fib_list[-1] < max_value:
        if fib_list[-1] > max_value:
            break
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])
    for num in fib_list:
        if num % 2 == 0:
            result.append(num)
    
    return sum(result)
    


print(even_fibonacci_numbers())