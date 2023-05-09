def alphabeticPos(letter, Aequals1=True):
    alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    if Aequals1 == True:
        return alphabet.index(letter.upper())+1
    else:
        return alphabet.index(letter.upper())

def toAlphabet(number, Aequals1=True):
    alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    if Aequals1 == True:
        return alphabet[int(number)-1]
    else:
        return alphabet[int(number)]


def caesarCipher(string, places):
    shifted = ''
    for char in string:
        if char == ' ':
            shifted += char
        else:
            shifted += toAlphabet((alphabeticPos(char.upper(), False)+places)%26, False)
    return shifted