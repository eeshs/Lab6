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
def decode(encoded_password):
    num = 0
    decoded_password = ' '
    for char in encoded_password:
        num = int(char) - 3
        decoded_password += str(num)
    return decoded_password
def menu_display():
    print("Menu \n ------------- \n 1. Encode \n 2. Decode \n 3. Quit\n")


if __name__ == '__main__':
    menu = 'Y'
    newnum = 0
    while menu != 'N':
        menu_display()
        choice = input("Enter a number")
        if choice == "1":
            number = (input("Please enter a number you would like to encode\n"))
            newnum = encode(number)
        elif choice == "2":
            decoded = decode(newnum)
            print(f"Your encoded password is {newnum} and the original password is {decoded}")
        elif choice == "3":
            break
        print("Your encoded number: " + newnum)
        menu = (input)("Would you like to continue?(Y or N)")

