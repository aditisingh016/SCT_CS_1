def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please run the program again.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be a number!")
        return

    if choice == '1':
        encrypted_msg = encrypt(message, shift)
        print("Encrypted Message:", encrypted_msg)
    else:
        decrypted_msg = decrypt(message, shift)
        print("Decrypted Message:", decrypted_msg)

# Run the program
main()
