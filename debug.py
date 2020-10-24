# import os
import datetime


def decorator_for_logging(file):
    def decorator(function_for_decorate):
        def return_parameters(*args, **kwargs):
            return str(args) + str(kwargs)

        def write_log(file, message):
            if file == '':
                print(message)
            else:
                with open(file, "a") as f:
                    f.write(message)

        def logging_function(*args, **kwargs):
            write_log(file,
                      f'Функция {function_for_decorate.__name__} вызвана в {datetime.datetime.now()} ' +
                      f'с параметрами {return_parameters(*args, **kwargs)}.')
            result = function_for_decorate(*args, **kwargs)
            write_log(file,
                      f' Завершена с результатом {str(result)} в {datetime.datetime.now()}.\n')
            return result
        return logging_function
    return decorator
