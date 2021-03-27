try:
    try:
        try:
            print('1' + 1)
        except Exception as exc:
            print("Exception level 3: ", exc)
            raise
    except Exception as exc:
        print("Exception level 2: ", exc)
        raise Exception("New message!")
except Exception as exc:
    print("Exception level 1: ", exc)
