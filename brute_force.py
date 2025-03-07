import itertools
import string

def decrypt(ciphertext, key):
   
    decryption_mapping = {cipher_char: plain_char for cipher_char, plain_char in zip(string.ascii_uppercase, key)}
    decrypted_text = []
    for char in ciphertext:
        if char in decryption_mapping:
            decrypted_text.append(decryption_mapping[char])
        else:
            decrypted_text.append(char)  
    return ''.join(decrypted_text)

def is_valid_plaintext(text):
    
    common_words = {"THE", "AND", "OF", "TO", "IN", "IS", "IT", "THAT", "FOR", "WITH"}
    words_in_text = text.upper().split() 
    return any(word in common_words for word in words_in_text)

# Brute-force attack (simplified)
def brute_force_attack(ciphertext):
    alphabet = string.ascii_uppercase
    
    subset_size = 3 
    for count, key_permutation in enumerate(itertools.permutations(alphabet, subset_size)):
        key = ''.join(key_permutation)
        decrypted_text = decrypt(ciphertext, key)
        if is_valid_plaintext(decrypted_text):
            print(f"Possible key found: {key}")
            print(f"Decrypted text: {decrypted_text}")
            return  
        if count % 1000 == 0:  
            print(f"Attempts: {count}, Current key: {key}, Decrypted: {decrypted_text}")
    print("No valid key found in the tested subset.")


if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ") 
    print("Starting brute-force attack...")
    brute_force_attack(ciphertext)
    