print("Добро пожаловать в калькулятор! Выберите операцию:")
print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")
print("5 - возведение в степень")

choice = input("Введите номер операции: ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))


def test():
    pass


def add(a, b):
    return a+b


def multiply(a, b):
    return a*b


def subtract(a, b):
    return float(a) - float(b)


def divide(a, b):
    if b != 0:
        return a/b
    return -1

  
def power(a, b):
    return(a**b)



match choice:
    case "1":
        print(add(a, b))
    case "2":
        print(subtract(a, b))
    case "3":   
        print(multiply(a, b))
    case "4":
        print(divide(a,b))
    case "5":
        print(power(a, b))
    case _:
        print("Неверный выбор")
