def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter the message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(message, shift)
print("Encrypted Message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Message:", decrypted_text)