numbers = []
size = 8
half = (size//2)

def number_zero():
    global size, half

    list_00 = []
    for i in range(size):
        line = ""
        for j in range(half+1):
            if i == 0 or i == (size-1) or j == 0 or j == half:
                line +="0 "
            else:
                line +="  "

        list_00.append(line.rstrip().ljust(9))
    return list_00


def number_one():
    global size, half

    list_01 = []
    for i in range(size): 
        line = ""

        for j in range(half+1):
            if j == half:
                line +="1 "
            else:
                line += "  "

        list_01.append(line.strip().ljust(9))
    return list_01

def number_two():
    global size, half
    list_02 = []
    

    for i in range(half):
        line = ""
        for j in range(half):
            if i == 0 or j == (half-1):
                line +="2 "
            else: line +="  "

        list_02.append(line.rstrip().ljust(9))
    

    for i in range(half):
        line = ""
        for j in range(half):
            if i == (half -1) or j == 0 or i == 0:
                line += "2 "
            else: 
                line += "  "
        list_02.append(line.rstrip().ljust(9))
    return list_02

myrange = input("Type")

for nums in myrange:
    if nums == "0":
        numbers.append(number_zero())
    elif nums == "1":
        numbers.append(number_one())
    elif nums == "2":
        numbers.append(number_two())




for row in range(size):
    #print(numbers[0][row] + "        "+ numbers[1][row]+"        "+numbers[2][row])
    line = ""
    for num in numbers:
        line += num[row]+ "    "
    print (line)

