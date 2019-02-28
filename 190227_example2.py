integer = 123
string = ''
while integer > 0:
    string = chr((integer % 10) + ord('0')) + string
    integer //= 10

print(string)