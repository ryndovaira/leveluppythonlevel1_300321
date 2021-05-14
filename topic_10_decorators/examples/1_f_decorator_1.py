# ---------------------------------- Создадим свой декоратор "вручную" ------------------------------------------------
def my_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, до вызова функции")
        result = function_to_decorate()  # Сама функция
        print("Я - код, срабатывающий после")

        if result is None:
            return 0

        return result + 111

    return the_wrapper_around_the_original_function


def constant_function():
    print("Я функция, которую ты не изменишь!")

    return 777


print("\nconstant_function:")
constant_function()
# Я функция, которую ты не изменишь!

decorated_function = my_decorator(constant_function)

print("\ndecorated_function:")
print(decorated_function())
# Я - код, до вызова функции
# Я функция, которую ты не изменишь!
# Я - код, срабатывающий после

my_decorator(constant_function)()

constant_function = my_decorator(constant_function)     # ДЕКОРАТОР!
print("\ndecorated constant_function:")
constant_function()
# Я - код, до вызова функции
# Я функция, которую ты не изменишь!
# Я - код, срабатывающий после


# ---------------------------------- Используем декоратор Python ------------------------------------------------------
# эквивалентно another_const_function = my_decorator(another_const_function)
@my_decorator       # - это декоратор
def another_const_function():
    print("Меня тоже нельзя менять!")


print("\ndecorated another constant_function:")
another_const_function()
# Я - код, до вызова функции
# Меня тоже нельзя менять!
# Я - код, срабатывающий после

