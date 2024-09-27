firs = input('введите число: ')
second = input('введите число:')
third = input('введите число:')
if firs == second == third:
    print(3)
elif firs==second or firs==third or second==third:
    print(2)
else:
    print(0)