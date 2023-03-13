def spam(divideBy):
    return 42 / divideBy


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


# tratando a exceção

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:

        print('Error: divisão por zero')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
