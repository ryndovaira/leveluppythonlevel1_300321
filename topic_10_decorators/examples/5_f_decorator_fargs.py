def my_decorator(function_to_decorate):
    def the_wrapper_function(arg1, arg2, arg3):
        print("Я получил: ", arg1, arg2, arg3)
        function_to_decorate(arg1, arg2)

    return the_wrapper_function


@my_decorator
def const_function_with_args(arg1, arg2):
    print("У меня есть: ", arg1, arg2)


# @my_decorator = const_function_with_args = my_decorator(const_function_with_args)

const_function_with_args("Первый", 2, 777)
# Я получил:  Первый 2
# У меня есть:  Первый 2
