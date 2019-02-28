character = '42FB'
length = len(character)
integer = 0
for i in range(length-1, -1, -1):
    if ord('0') <= ord(character[i]) <= ord('9'):
        integer += (ord(character[i])-ord('0'))*16**(length-i-1)
    elif ord('A') <= ord(character[i]) <= ord('F'):
        integer += ((ord(character[i])-ord('A'))+10)*16**(length-i-1)

print(integer)
