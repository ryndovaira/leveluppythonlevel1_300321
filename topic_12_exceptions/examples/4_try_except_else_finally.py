for i in range(3):
    try:
        val = int(input("input number: "))
        tmp = 10 / val
        print(tmp)
    except ZeroDivisionError as div_exc:
        print("ZeroDivisionError: ", div_exc)
    except Exception as ex:
        print("Unknown Error: ", ex)
    except:     # плохой стиль!
        print("Unknown Error!")
    else:   # если ошибки не было
        print("Result = ", tmp)
        break
    finally:   # выполнить в любом случае
        print('Finally code')
