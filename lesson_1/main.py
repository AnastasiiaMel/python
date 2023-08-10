def calculate_sum(a: float, b: float):
    result = a + b
    return result


if __name__ == '__main__':
    """    
    My first program by python
    """
    print('Hello world')  # Эта строка печатает привет мир

    a: int = 5
    b = 6
    print(a + b)

    a: float = float(input('Введите а '))
    b = float(input('Введите b '))
    print(a / b)

    a: float = float(input('Введите а '))
    b = float(input('Введите b '))
    if b == 0:
        print('Нельзя разделить на ноль!')
    else:
        print(a / b)

    print(calculate_sum(a, b))
