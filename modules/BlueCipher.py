#Step1: Tridigital Cipher
def bluecipherstep1(display2, display3, display4, numofindicators):
  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  key = []
  [key.append(x) for x in display4 if x not in key]
  key = ''.join(key)

  alphabetfixed = []
  [alphabetfixed.append(x) for x in alphabet if x not in key]
  alphabetfixed = ''.join(alphabetfixed)

  if numofindicators%2 == 0:
    key += alphabetfixed
  else:
    key = alphabetfixed + key

  table = [key[0:9], key[9:18], key[18:25]]

  decrypt1 = ''
  for i in range(0, 6):
    decrypt1 += table[int(display2[i])-1][int(display3[i])-1]
  return decrypt1

#Step 2: Atbash Cipher
def bluecipherstep2(display1):
  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  encrypt1 = ''
  for char in display1:
    encrypt1 += alphabet[25-alphabet.index(char)]
  return encrypt1

#Step 3: Vigenere Cipher
def bluecipherstep3(decrypt1, encrypt1):
  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  decrypted = ''
  for i in range(0, 6):
    decrypted += alphabet[(alphabet.index(encrypt1[i])-alphabet.index(decrypt1[i])-1)%26]
  return decrypted

def bluecipher(display1, display2, display3, display4, numofindicators):
  decrypt1 = bluecipherstep1(display2, display3, display4, numofindicators)
  encrypt1 = bluecipherstep2(display1)
  return bluecipherstep3(decrypt1, encrypt1)

def run():
    display1 = input("What does the First display say?: ").upper()
    display2 = input("What does the Second display say?: ")
    display3 = input("What does the Third display say?: ")
    display4 = input("What does the Fourth display say?: ").upper()
    numofindicators = int(input("What is the Number of Indicators?: "))
    print('The Decrypted word is:', bluecipher(display1, display2, display3, display4, numofindicators))
