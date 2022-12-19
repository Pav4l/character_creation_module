from math import sqrt

message: str = '''
Добро пожаловать в самую лучшую программу для вычисления
 квадратного корня из заданного числа
'''
print(message)


def calculatesquareroot(number: float) -> float:
    """Вычисляет квадратный корень."""

    return sqrt(number)


def calc(your_number: float) -> str:
    """Возвращает результат вычислений с комментариями."""

    if your_number <= 0:
        return f'Некорректное значение.'
    calculate: float = calculatesquareroot(your_number)
    return f'Мы вычислили квадратный корень из введённого вами числа. Это будет: {calculate}'


calc(25.5)
