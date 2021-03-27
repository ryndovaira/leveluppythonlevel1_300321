import traceback


class NegValException(Exception):
    """Content: NegValException"""
    pass


try:
    val = int(input("input positive number: "))
    if val < 0:
        raise NegValException("Neg val: " + str(val))
    print(val + 10)
except NegValException as e:
    print(e)
    print(e.__traceback__)  # <traceback object at 0x7fc1318d6aa0>
    traceback.print_tb(e.__traceback__)
