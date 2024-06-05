def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e) encrypt or (d) decrypt a message? (q to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

# 🔐 Exploring Classical Cryptography with Python!

# I'm excited to share a recent project where I implemented a Caesar Cipher in Python. This classic encryption technique, named after Julius Caesar, shifts each letter in a message by a set number of places. It’s a great way to grasp the basics of cryptography and enhance Python skills.

# Key Features:
# Encrypt/Decrypt Functions: Shift letters based on a user-defined value.
# User Interaction: Easily choose to encrypt or decrypt messages.
# Educational Value: Perfect for learning fundamental concepts in data security.
# This project blends historical cryptographic methods with modern programming, making it both fun and educational. Check out the full project on my GitHub here.

# #Python #Cryptography #Programming #Tech