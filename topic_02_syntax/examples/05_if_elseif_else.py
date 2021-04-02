num = int(input('Enter number: '))

if num > 0:
    sign = "positive"
elif num == 0:
    sign = 'zero'
else:
    sign = 'negative'

print(f'{num} is a {sign} number.')

# You can do
# print('{n} is a {s} number.'.format(n=num, s=sign))
