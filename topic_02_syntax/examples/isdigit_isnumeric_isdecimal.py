def check_str(my_str):
    print(f"mystr: {my_str}")
    print(f"isnumeric: {str.isnumeric(my_str)}")
    print(f"isdecimal: {str.isdecimal(my_str)}")
    print(f"isdigit: {str.isdigit(my_str)}")
    print("-" * 50)


# isdecimal() ⊆ isdigit() ⊆ isnumeric()
if __name__ == '__main__':
    check_str('½')
    check_str('ⅠⅢⅧ')
    check_str('⑩⑬㊿')

    check_str('³')
    check_str('🄀⒊⒏')
    check_str('⓪③⑧')

    check_str('038')
    check_str('０３８')  # FULLWIDTH DIGIT
    check_str('٠١٢٣٤')  # ARABIC-INDIC DIGIT

    check_str('-38')
    check_str('+38')
    check_str('3_8')
