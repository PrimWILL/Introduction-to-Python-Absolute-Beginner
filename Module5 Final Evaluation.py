def adding_report(str = "T"):
    if str == "T":
        total = 0
        while True:
            items = input('Enter an integer or "Q": ')
            if items.isdigit():
                total = total + int(items)
            elif ('Q' <= items < 'R' or 'q' <= items < 'r') == True:
                print('\nTotal\n',total)
                break
            else:
                print(items, 'is invalid input')
    elif str == "A":
        res = ''
        total = 0
        while True:
            items = input('Enter an integer or "Q": ')
            if items.isdigit():
                total = total + int(items)
                res = res + items +"\n"
            elif ('Q' <= items < 'R' or 'q' <= items < 'r') == True:
                print('\nItems\n', res)
                print('Total\n', total)
                break
            else:
                print(items, 'is invalid input')


print('Report Types include All Items ("A") or Total Only ("T")')
while True:
    at = input('Choose Report Type ("A" or "T"): ')
    if at == "A":
        print('Input an integer to add to the toal or "Q" to quit')
        adding_report(at)
        break
    elif at == "T":
        print('Input an integer to add to the toal or "Q" to quit')
        adding_report(at)
        break
    else:
        print(at, 'is invalid input')

