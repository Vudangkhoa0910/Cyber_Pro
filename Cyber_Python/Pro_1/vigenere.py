def vigenere_encrypt(text, key):
    result = []
    key = key.upper()
    key_length = len(key)
    key_index = 0
    steps = []

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(encrypted_char)
            steps.append(f"{char} -> {encrypted_char} (Shift: {shift})")
            key_index += 1
        else:
            result.append(char)

    return ''.join(result), '<br>'.join(steps)

def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    key_length = len(key)
    key_index = 0
    steps = []

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift + 26) % 26 + start)
            result.append(decrypted_char)
            steps.append(f"{char} -> {decrypted_char} (Shift: {shift})")
            key_index += 1
        else:
            result.append(char)

    return ''.join(result), '<br>'.join(steps)
