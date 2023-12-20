def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2      # сложение
    elif operator == '-':
        return value1 - value2      # вычитание
    elif operator == '*':
        return value1 * value2      # умножение
    elif operator == '/':
        return value1 / value2      # деление

# тест
print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))