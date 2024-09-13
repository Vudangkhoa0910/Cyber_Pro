def caesar_encrypt(text, shift):
    shift = shift % 26
    result = ""
    steps = []

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result += encrypted_char
            steps.append(f"'{char}' -> '{encrypted_char}' (Shift: {shift})")
        else:
            result += char

    return result, '<br>'.join(steps)

def caesar_decrypt(text, shift):
    shift = shift % 26
    result = ""
    steps = []

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift + 26) % 26 + start)
            result += decrypted_char
            steps.append(f"'{char}' -> '{decrypted_char}' (Shift: {shift})")
        else:
            result += char

    return result, '<br>'.join(steps)
