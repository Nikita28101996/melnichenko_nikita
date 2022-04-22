num = range(101)
for num in list(range(len(num))):
    if num >= 11 and num <= 14:
        print(num, 'процентов')
    elif num % 10 == 1:
            print(num, 'процент')
    elif num % 10 >= 2 and num % 10 <= 4:
            print(num, 'процента')
    else:
            print(num, 'процентов')