#A Letter
def ALetter(Serial, First_Letter):
  FirstDigit = 0
  for char in Serial:
    if char.isdigit():
      FirstDigit = int(char)
      break

  FirstLetter = ''
  for char in Serial:
    if 64 < ord(char) < 91:
      FirstLetter = char
      break

  alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
  RemainingList = alphabet.copy()
  Solution = ''
  Solution += RemainingList.pop(alphabet.index(First_Letter))
  Solution += RemainingList.pop(alphabet.index(FirstLetter))
  Solution += RemainingList.pop(FirstDigit-1)
  for i in range(0, len(RemainingList)-1):
    Solution += RemainingList.pop(alphabet.index(Solution[len(Solution)-3])%len(RemainingList))
  Solution += RemainingList[0]
  return Solution

def run():
    Serial = input('Whats the Serial Number?: ').upper()
    First_Letter = input('Whats the First Letter?: ').upper()
    print("Your Solution Sequence is: ", ALetter(Serial, First_Letter))
