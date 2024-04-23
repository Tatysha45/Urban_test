import warnings

a = 10
b = 0.01
def safe_division(a, b):
    if b <= 0.01:
        warnings.warn('делитель близок к нулю')
        print(warnings.warn)
        return None
    else:
        return a / b


#warnings.simplefilter("error")
#warnings.simplefilter("ignore")
warnings.simplefilter("always")


try:
    safe_division(a, b)
    print("выполнение продолжается")
except warnings.warn:
    print()