import re

def create_playfair_matrix(key):
    key = key.upper().replace("J", "I")  
    key = re.sub(r"[^A-Z]", "", key)  
    key = "".join(dict.fromkeys(key)) 

    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = re.sub(r"[^A-Z]", "", text) 
    text = re.sub(r"(.)\1", r"\1X\1", text)  
    if len(text) % 2 != 0:
        text += "X"  
    return text

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None
def encrypt_digraph(matrix, digraph):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b: 
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else: 
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def decrypt_digraph(matrix, digraph):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:  
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:  
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else: 
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def encrypt_playfair(plaintext, matrix):
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_digraph(matrix, plaintext[i:i+2])
    return ciphertext

def decrypt_playfair(ciphertext, matrix):
    ciphertext = prepare_text(ciphertext)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_digraph(matrix, ciphertext[i:i+2])
    return plaintext

if __name__ == "__main__":
  choice = input("1.Encrypt \n 2.Decrypt\n(1,2): ").strip().lower()
    if choice not in ["1", "2"]:
        print("Invalid choice. Please enter '1' for encrypt or '2' for decrypt.")
        exit()

    key = input("Enter the key: ").strip()
    matrix = create_playfair_matrix(key)
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(" ".join(row))

    text = input(f"Enter the text to {'encrypt' if choice == '1' else 'decrypt'}: ").strip()

    if choice == "1":
        result = encrypt_playfair(text, matrix)
        print("\nEncrypted text:", result)
    else:
        result = decrypt_playfair(text, matrix)
        print("\nDecrypted text:", result)
