def ceaser_cipher(text, shift, mode):
        if mode == 'encrypt':
            result = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = ord('a') if char.islower() else ord('A')
                    result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    result += char
            return result
        elif mode == 'decrypt':
            result = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = ord('a') if char.islower() else ord('A')
                    result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    result += char
            return result
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            return None
    
while (True):
        number = int(input("\n1. Encrypt\n2. Decrypt\n3.terminate the program\npleese choose a number :"))
        if (number == 1):
            text = input("please enter the text :")
            shift = int(input("please enter the shift :"))
            result = ceaser_cipher(text, shift, mode='encrypt')
            print(result)
            continue
        elif number == 2:
            text = input("please enter the text :")
            shift = int(input("please enter the shift :"))
            result = ceaser_cipher(text, shift, mode='decrypt')
            print(result)
            continue
        elif number == 3:
            print("program terminated successfully!")
            break
        else:
            print("please choose a valid number.")
            continue