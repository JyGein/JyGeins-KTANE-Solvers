from math import ceil
#Magenta Cipher, Step 1: Affine Cipher
def magentacipherstep1(Serial, display1, display2):
  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  E = display2
  sSum = 0

  for char in Serial:
    if char.isdigit():
      sSum += int(char)
  X = sSum%26+1

  for i in range(0, 101):
    if (E*i)%26 == 1:
      D = i
      break

  encrypt2 = ''
  for char in display1:
    encrypt2 += alphabet[(((alphabet.index(char)+1)-X)*D)%26-1]
  return encrypt2

#Step 2: Myszkowski Transposition
def magentacipherstep2(Serial, encrypt2):
  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  key = ''
  for char in Serial:
    if char.isdigit() == False:
      key += char

  keydict = {}
  sortedkey = ''.join(sorted(set(key)))
  keyleft = len(key)
  dashesleft = 6

  count = 0
  for char in key:
    keydict[count] = [sortedkey.index(char), ceil(dashesleft/keyleft)]
    keyleft -= 1
    dashesleft -= keydict[count][1]
    count += 1
  soldict = {}
  for k in keydict:
    soldict[k] = ''

  count1 = 0
  hasdashes = {}
  while count1 < 6:
    sortedkeydict = []
    for f in range(0, len(keydict)):
      if keydict[f][0]==0 and keydict[f][1]>0:
        sortedkeydict += [sorted(keydict.items())[f]]
    if sortedkeydict==[]:
      for k in keydict:
        keydict[k][0] -= 1
      for f in range(0, len(keydict)):
        if keydict[f][0]==0 and keydict[f][1]>0:
          sortedkeydict += [sorted(keydict.items())[f]]
    for i in sortedkeydict:
      soldict[i[0]] += encrypt2[count1]
      keydict[i[0]][1] -= 1
      count1 += 1

  encrypt3 = ''
  count = 0
  for i in range(0, ceil(6/len(key))):
    for k in soldict:
      if count == 6:
        break
      count += 1
      encrypt3 += soldict[k][i]
  return encrypt3

#Step 3: Autokey Cipher
def magentacipherstep3(display3, encrypt3):
  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  key = display3
  decrypted = ''
  for i in range(0, 6):
    letter = alphabet[(((alphabet.index(encrypt3[i])+1)-(alphabet.index(key[i])+1))%26)-1]
    key += letter
    decrypted += letter
  return decrypted

def magentacipher(Serial, display1, display2, display3):
  encrypt2 = magentacipherstep1(Serial, display1, display2)
  encrypt3 = magentacipherstep2(Serial, encrypt2)
  return magentacipherstep3(display3, encrypt3)

def run():
    Serial = input("What is the Serial Number?: ")
    display1 = input("What does the First display say?: ")
    display2 = int(input("What does the Second display say?: "))
    display3 = input("What does the Third display say?: ")
    return magentacipher(Serial, display1, display2, display3)