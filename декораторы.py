def is_prime_decorator(sum_three):
    def wrapper(*args, **kwargs):
        result = sum_three(*args, **kwargs)
        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")

        return result
    return wrapper


print()

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c


result = sum_three(3, 7, 5)
print(result)