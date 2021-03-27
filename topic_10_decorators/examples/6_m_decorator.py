def method_decorator(method_to_decorate):
    def wrapper(self, bonus):
        bonus *= 2
        return method_to_decorate(self, bonus)

    return wrapper


class Seller:
    def __init__(self):
        self.price = 30

    @method_decorator
    def tell_price(self, bonus):
        print("Это стоит всего {}$"
              .format(self.price + bonus))


s = Seller()
s.tell_price(bonus=10)
# Это стоит всего 50$
