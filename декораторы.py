from math import isqrt

def is_prime_decorator(sum_three):
    def wrapper(*args, **kwargs):
        result = sum_three(*args, **kwargs)
        if result <= 1:
            print(f"Результат {result} функции {sum_three.__name__} простое число")
            return result
        for i in range(2, isqrt(result) + 1):
            if result % i == 0:
                print(f"Результат {result} функции {sum_three.__name__} составное число")
                return result

        return result
    return wrapper
print()

@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c


result = sum_three(3, 7, 5)
print(result)









# def sum_three(a, b, c):
#     return a + b + c
# numbers = [3, 7, 5]
# sum = sum(numbers)
# n = numbers