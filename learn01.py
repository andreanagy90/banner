size = 8
half = (size//2)

def number_zero():
    global size, half

    # for i in range(half):
    #     for j in range (half+1):
    #         if i == 0 or j == half or j == 0:
    #             print("0 ",end="")
    #         else:
    #             print("  ", end="")
    #     print()
    
    # for i in range(half):
    #     for j in range (half+1):
    #         if i == half-1 or j == 0 or j == half:
    #             print("0 ",end="")
    #         else:
    #             print("  ", end="")
    #     print()

    for i in range(size):
        for j in range(half+1):
            if i == 0 or i == (size-1) or j == 0 or j == (half):
                print("0 ", end="")
            else:
                print("  ", end="")
        print()
    print (end="")
    print()

def number_one():
    global size
    for i in range(size):
        print("1", end="")
        print()
    print (end="")
    print()
def number_two():
    global size, half
    

    for i in range(half):
        for j in range(half):
            if i == 0 or j == half-1:
                print("2 ",end="")
            else: print("  ",end="")

        print()
    print()
    for i in range(half):
        for j in range(half):
            if i == half -1 or j == 0 or i == 0:
                print("2 ",end="")
            else: print("  ",end="")
            
        print()
    print (end="")
    print()

def number_three():
    
    global size, half
    
    for k in range (2):
        for i in range(half):
            for j in range(half+1):
                if i == 0 or j == half or i == half-1:
                    print ("3 ", end="")
                else:
                    print("  ", end="")
            print()

    print (end="")

def number_four():
    global size, half
    for i in range(half):
        for j in range(half+1):
            if i == (half-1) or j == 0:
                print("4 ", end="")
            else:
                print("  ", end="")
        print()
    
    for i in range(half):
        for j in range(half+1):
            if j == (half):
                print("4 ", end="")
            else:
                print("  ", end="")
        print()
    
    print (end="")

def number_five():
    global size,half    

    for i in range(half):
        for j in range(half+1):
            if i == 0 or i == (half-1) or j == 0:
                print("5 ",end="")
            else:
                print("  ", end="")
        print()
    
    for i in range(half):
        for j in range(half+1):
            if i == (half-1) or j == half:
                print("5 ", end="")
            else:
                print("  ", end="")
        print()
    print (end="")

def number_six():
    pass
# number_one()
# number_two()
# number_three()
#number_four()
#number_five()

run = True

def user ():
    global run
    list = []

    number = input("Type your number to draw: ")
    for n in str(number):
        if n == "1":
            list.append(number_one())
        elif n == "2":
            list.append(number_two())
        elif n == "3":
            list.append(number_three())
        elif n == "4":
            list.append(number_four())
        elif n == "5":
            list.append(number_five())
        elif n == "0":
            list.append(number_zero())
        elif n == "q" or number == "Q":
            run = False
    
    for l in list:
        pass
        

while run:
    user()