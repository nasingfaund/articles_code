def add(x, y):
    """Функция сложения"""
    return x + y

def subtract(x, y):
    """Функция вычитания"""
    return x - y

def multiply(x, y):
    """Функция умножения"""
    return x * y

def divide(x, y):
    """Функция деления"""
    if y == 0:
        return "Ошибка: Деление на ноль!"
    return x / y

def main():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    while True:
        choice = input("Введите номер операции (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            
            next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
            if next_calculation.lower() != 'да':
                break
        else:
            print("Неправильный ввод. Пожалуйста, введите номер операции.")

if __name__ == "__main__":
    main()
