# your Python implemnetation of the programming assignment 
# note: Do only one implemention, do not implement C++ if you complete the Pyhton code.

def generate_numbers(base, number_of_digits, limit):
    if base not in [2, 8, 10, 16]:
        print("Invalid base. Please choose 2, 8, 10, or 16.")
        return

    base_characters = [str(i) for i in range(base)] + [chr(ord('A') + i) for i in range(6)] if base == 16 else [str(i) for i in range(base)]
    base_name = "binary" if base == 2 else "octal" if base == 8 else "decimal" if base == 10 else "hexadecimal"

    print(f"Base-{base} Alphabet: {base_characters}")
    print(f"Rule for Base-{base}:")
    print(f"The first digit goes up to {base_characters[-1]}, "
          f"then the digit is reset to {base_characters[0]}, and 1 is carried to the next digits. "
          f"If the carry is to a digit that is already {base_characters[-1]}, "
          f"then that digit is also reset from {base_characters[0]} to {base_characters[-1]} "
          f"and is carried to the next digit.")

    current_number = [base_characters[0]] * number_of_digits

    try:
        limit_num = int(limit, base)
    except ValueError:
        print(f"Invalid character in limit value for base {base}.")
        print(f"Valid base-{base} Alphabet: {base_characters}")
        return

    while int(''.join(current_number), base) < limit_num:
        carry = 1
        carry_str = ""
        for i in range(number_of_digits - 1, -1, -1):
            current_char = current_number[i]

            # Find the index of the current character
            char_index = -1
            for j in range(len(base_characters)):
                if base_characters[j] == current_char:
                    char_index = j
                    break

            if char_index == -1:
                print("Invalid character in current_number.")
                return

            # Calculate the new index and carry
            new_index = (char_index + carry) % len(base_characters)
            carry = (char_index + carry) // len(base_characters)

            # Update the current character
            current_number[i] = base_characters[new_index]

            if carry == 1:
                carry_str += "(Reset, carry)"

        current_number_str = ''.join(current_number)
        if int(current_number_str, base) < limit_num:
            print(f"{current_number_str} {carry_str}")

base = int(input("Enter the base (2, 8, 10, or 16): "))
number_of_digits = int(input("Enter the number of digits: "))
limit = input(f"Enter the limit (in base {base}): ")

generate_numbers(base, number_of_digits, limit)
