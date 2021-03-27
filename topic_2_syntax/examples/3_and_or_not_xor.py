a = True
b = False
c = False
d = True

print(f"a={a}\tb={b}\tc={c}\td={d}")

print(f"{'-' * 50}")
print('a and b and c =>', a and b and c)
print('b and c =>', b and c)
print('a and d =>', a and d)

print(f"{'-' * 50}")
print('a or b =>', a or b)
print('b or c =>', b or c)

print(f"{'-' * 50}")
print('not a =>', not a)
print('not b =>', not b)

print(f"{'-' * 50}")
print('a xor b =>', a != b)
print('b xor c =>', b != c)
print('a xor d =>', a != d)

print()
# побитовый XOR - НЕ ПУТАТЬ
print('a xor b =>', a ^ b)
print('b xor c =>', b ^ c)
print('a xor d =>', a ^ d)
