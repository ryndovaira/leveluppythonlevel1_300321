string = "outer"
def set():
    pass
    string = "inner"

set()
print(string)   # 'outer'