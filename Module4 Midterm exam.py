guess = 99

def STR_ANALYSIS(str):
    if str.isdigit():
        str = int(str)
        if str > 99:
            return print(str, "is a pretty big number")
        elif str < 99:
            return print(str, "is a smaller number than expected")
        else:
            return print("Correct! Congratulation.")
    elif str.isalpha():
        return print("\""+str+"\" is all alphabetical characters!")
    else:
        return print("\""+str+"\" is a surprise! It's neither all all alpha nor all digit characters!")

while True:
    string = input("enter word or integer: ")
    if string != '':
        STR_ANALYSIS(string)
        break
    else:
        pass