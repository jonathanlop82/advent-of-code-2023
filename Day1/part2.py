import re

with open('data.txt') as f:
    lines = f.readlines()

numbers = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','1','2','3','4','5','6','7','8','9']
match = {

}
total = 0
for line in lines:
    first = 0
    last = 0
    first_number = len(line) + 1
    last_number = 0
    for number in numbers:
        if number in line:
            lista = [m.start() for m in re.finditer(r'{}'.format(re.escape(number)), line)]
            result_first = min(lista)
            result_last = max(lista)
            if result_first < first_number:
                first_number = result_first
                first = numbers.index(number)
                if first > 9:
                    first = number
            if result_last >= last_number:
                last_number = result_last
                last = numbers.index(number)
                if last > 9:
                    last = number

    '''
    for leter in reverse:
        d = unicode(leter, 'utf-8')
        if d.isnumeric():
            result = len(reverse) - reverse.index(leter) - 1
            print(result)
            print(last_number)
            if result > last_number:
                last_number = result
                last = leter
    '''   

    num = int(str(first)+ str(last))
    total = total + num

print(total)