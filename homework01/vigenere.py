"""
Шифр виженера реализован с помощью значений символов в Unicode
"""
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    key_index = 0
    for i in plaintext:
        if "A" <= i <= "Z":
            ciphertext += chr((ord(i) - ord("A") + (ord(keyword[key_index]) - \
                                                    ord("A"))) % 26 + ord("A"))
            key_index = key_index + 1
            key_index = key_index % len(keyword)
        elif "a" <= i <= "z":
            ciphertext += chr((ord(i) - ord("a") + (ord(keyword[key_index]) - \
                                                    ord("A"))) % 26 + ord("a"))
            key_index = key_index + 1
            key_index = key_index % len(keyword)
        else:
            ciphertext = ciphertext + i
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    key_index = 0
    for i in ciphertext:
        if "A" <= i <= "Z":
            plaintext += chr((ord(i) - ord("A") - (ord(keyword[key_index]) - \
                                                   ord("A"))) % 26 + ord("A"))
            key_index = key_index + 1
            key_index = key_index % len(keyword)
        elif "a" <= i <= "z":
            plaintext += chr((ord(i) - ord("a") - (ord(keyword[key_index]) - \
                                                   ord("A"))) % 26 + ord("a"))
            key_index = key_index + 1
            key_index = key_index % len(keyword)
        else:
            plaintext = plaintext + i
    return plaintext
