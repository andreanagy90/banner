numbers = []
size = 8
half = (size//2)

def number_zero():
    global size, half
                        # Comments for my project/Kommentjeim a projektemhez
    list_00 = []        # Create list to rows/lista készítése a soroknak

                        # Drawing/Rajzolás
    for i in range(size):
        line = ""       # start with new line / Kezdje mindíg új sorba
        for j in range(half+1):
            if i == 0 or i == (size-1) or j == 0 or j == half:
                line +="0 " #Add to line/ adja a sorhoz
            else:
                line +="  "

        list_00.append(line.rstrip().ljust(9)) #Add to list my lines / Adja a listához a sort
    return list_00          #Return to "list_00" / Adja vissza a lista értékét


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

        list_01.append(line.rstrip().ljust(9))
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


def number_three():
    
    global size, half
    list_03 = []
    

    for i in range(half):
        line =""
        for j in range(half+1):
            if i == 0 or j == half or i == (half-1):
                line +="3 "
            else:
                line +="  "
        list_03.append(line.rstrip().ljust(9))

    for i in range(half):
        line =""
        for j in range(half+1):
            if j == half or i == (half-1):
                line +="3 "
            else:
                line +="  "
        list_03.append(line.rstrip().ljust(9))
    
    return list_03


def number_four():
    global size, half
    list_04 = []
    for i in range(half):
        line = ""
        for j in range(half+1):
            if i == (half-1) or j == 0:
                line += "4 "
            else:
                line += "  "
        list_04.append(line.rstrip().ljust(9))
    
    for i in range(half):
        line =""
        for j in range(half+1):
            if j == (half):
                line +="4 "
            else:
                line +="  "
        list_04.append(line.rstrip().ljust(9))
    
    return list_04

def number_five():
    global size,half   
    list_05 = [] 

    for i in range(half):
        line =""
        for j in range(half+1):
            if i == 0 or i == (half-1) or j == 0:
                line += "5 "
            else:
                line += "  "
        list_05.append(line.rstrip().ljust(9))
    
    for i in range(half):
        line = ""
        for j in range(half+1):
            if i == (half-1) or j == half:
                line +="5 "
            else:
                line +="  "
        list_05.append(line.rstrip().ljust(9))
    return list_05











myrange = input("Type your number to draw:  ") # User input/ Felhasználó bevitele

            # Loop trought in user input/ menjen végig a bevitel karakterein
for nums in myrange:
    if nums == "0":                   # If input:/Ha a bevitel ez: 
        numbers.append(number_zero()) # Add to Numbers list/ Adja a számok listájához
    elif nums == "1":
        numbers.append(number_one())
    elif nums == "2":
        numbers.append(number_two())
    elif nums == "3":
        numbers.append(number_three())
    elif nums == "4":
        numbers.append(number_four())
    elif nums == "5":
        numbers.append(number_five())



                        #Loop in numbers and add rows/ Menjen végig a numbers -en és vegye fel
                        #Print lines/Nyomtassa ki a sorokat
    

for row in range(size):
    line = ""
    for num in numbers:
        line += num[row]+ "     "
    print (line)
