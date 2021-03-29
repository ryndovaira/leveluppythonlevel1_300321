string = "outer"
def set():
    global string
    string = "inner"

set()
print(string)   # 'inner'