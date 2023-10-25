def encode(number):
    newnum = ''
    for char in number:
        if ((int)(char)+3) < 10:
            newchar = (int)(char)+3
            newnum += (str)(newchar)
        elif ((int)(char)+3) > 9:
            newchar = (int)(char) - 7
            newnum += (str)(newchar)
    return newnum
#if __name__ == 'main':
menu = 'Y'
while menu != 'N':
    number = (input)(print("Please enter a number you would like to encode"))
    newnum = encode(number)
    print("Your encoded number: " + newnum)
    menu = (input)("Would you like to continue?(Y or N)")