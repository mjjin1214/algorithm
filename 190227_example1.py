string = list('Reverse this strings')
length = len(string)
for i in range(length//2):
    string[i], string[length-i-1] = string[length-i-1], string[i]

print(''.join(string))