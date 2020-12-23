''' Octal basic operations (+) (-) (*) (/) (%) '''

user_numbers = int(input("how many octal numbers ?\n\n"))
list_1 = []

print("\n\n")

for num in range(1, user_numbers+1):
    input_num = input(f"{num}- ")
    list_1.append(input_num)

flag = 0
Addition = 0
Multiplication = 1

# converting to octal
for item in list_1:

    for char in item:

        if int(char) in range(8):
            char = oct(int(char))
            char = item[0]
            flag += 1
            break

        else:
            print(f"{item} is not an octal number")
            break

# Operations
while flag == len(list_1):

    menu = input(
        "\n\n1-Basic operations\n\n2-press q to exit\n\nEnter your choice : ")

    if(menu == 'q'):
        break

    elif int(menu) == 1:

        # Basic operations
        ch1 = input(
            "\n\n\n\n1-Addition (+)\n\n2-Substraction (-)\n\n3-Multiplication (*)\n\n4-Division (/)\n\n5-Modulus\n\nEnter your choice : ")

        # addition
        if int(ch1) == 1:

            for item in list_1:
                Addition += int(item, 8)

            print(
                f"\n\n\nthe Addition in decimal is : {Addition}\n\nthe Addition in octal is : {oct(Addition)}\n\n")

        # substraction
        elif int(ch1) == 2:
            first_num = int(list_1[0], 8)

            for item in list_1:
                first_num -= int(item[0:], 8)

            total_substract = first_num
            first_num = int(list_1[0], 8)
            total_substract += first_num

            print(
                f"the Substraction in decimal is : {total_substract}\nthe Substraction in octal is : {oct(total_substract)}\n\n")

        # Multiplication
        elif int(ch1) == 3:

            for item in list_1:
                Multiplication *= int(item, 8)

            print(
                f"the  Multiplication in decimal is : {Multiplication}\nthe  Multiplication in octal is : {oct(Multiplication)}\n\n")

        # Division
        elif int(ch1) == 4:
            first_num = int(list_1[0], 8)

            for item in list_1:
                first_num /= int(item, 8)

            total_division = first_num
            first_num = int(list_1[0], 8)
            total_division *= first_num

            print(
                f"the Divisionin decimal is : {float(total_division)}\nthe   Division in octal is : {oct(int(total_division))}\n\n")

        # Modulus
        elif int(ch1) == 5:
            first_num = int(list_1[0], 8)

            for item in list_1:
                total_mod = first_num % int(item, 8)

            print(
                f"the  Modulus in decimal is : {total_mod}\nthe  Substraction in octal is : {oct(int(total_mod))}\n\n")

    else:
        print("error , you didn't choose any of the functions \n\n")
