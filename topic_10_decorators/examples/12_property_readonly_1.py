class Mine(object):

    def __init__(self):
        self._x = 'some value'

    @property
    def prop(self):
        """
        It's my prop!
        """
        return self._x


def main():
    print(type(Mine.prop))
    # <class 'property'>

    print(help(Mine.prop))
    # Help on property: None

    mine = Mine()
    print(mine.prop)  # some value

    try:
        mine.prop = 'other value'
        # AttributeError: can't set attribute
    except Exception as ex:
        print(f"Exception: {ex}")
    else:
        print("It's miracle!")
    finally:
        print("Thanks 1!")

    try:
        del mine.prop
        # AttributeError: can't delete attribute
    except AttributeError as ex:
        print(f"AttributeError: {ex}")
        print("You can't do: del mine.prop")
    else:
        print("It's miracle!")
    finally:
        print("Thanks 2!")


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
    else:
        print("Everything was OK")
    finally:
        print("Thanks!!!")
