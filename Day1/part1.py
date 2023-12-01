with open('data.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    reverse = line[::-1]
    for leter in line:
        if leter.isnumeric():
            num = leter
            break

    for leter in reverse:
        if leter.isnumeric():
            num = num + leter
            break

    total = total + int(num)

print(total)