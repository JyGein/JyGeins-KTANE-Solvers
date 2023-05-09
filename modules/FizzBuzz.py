def FizzBuzz(number, amount, phrase):
  if number%amount == 0:
    return phrase
  else:
    return ''
def FizzBuzzGame(number):
  output = ''
  output += FizzBuzz(number, 3, 'Fizz')
  output += FizzBuzz(number, 5, 'Buzz')
  if output == '':
    output = number
  return output
def run():
    display1 = input('What does display one say?: ')
    display2 = input('What does display two say?: ')
    display3 = input('What does display three say?: ')
    display1color = input('What color is display one? (red/green/blue/yellow/white): ').lower()
    display2color = input('What color is display two? (red/green/blue/yellow/white): ').lower()
    display3color = input('What color is display three? (red/green/blue/yellow/white): ').lower()
    booleans = [('batteryHolders', bool(input('Are there 3 or more battery holders? (True or False): ') != 'False')), ('SerialParallel', bool(input('Is there a Serial and Parallel port? (True or False): ') != 'False')), ('SerialNum', bool(input('Are there 3 letters are 3 digits in the Serial Number? (True or False): ') != 'False')), ('DviStereo', bool(input('Is there a Dvi-D and a Stereo RCA port? (True or False): ') != 'False')), ('Strikes', bool(input('Are there 2 or more strikes? (True or False): ') != 'False')), ('Batteries', bool(input('Are there 5 or more batteries? (True or False): ') != 'False'))]
    display1 = [i for i in display1]
    display2 = [i for i in display2]
    display3 = [i for i in display3]
    colors = {'red': [7, 3, 4, 2, 6, 1, 3], 'green': [3, 4, 5, 3, 6, 2, 1], 'blue': [2, 9, 8, 7, 1, 2, 8], 'yellow': [4, 2, 8, 9, 2, 5, 3], 'white': [5, 8, 2, 1, 8, 3, 4]}  
    for k in range(0, len(booleans)):
        if booleans[k][1]:
            for i in range(0, len(display1)):
                display1[i] = str((int(display1[i])+colors[display1color][k])%10)
            for i in range(0, len(display2)):
                display2[i] = str((int(display2[i])+colors[display2color][k])%10)
            for i in range(0, len(display3)):
                display3[i] = str((int(display3[i])+colors[display3color][k])%10)
    count = 0
    for k in booleans:
        count += k[1]
    if count == 0:
        for i in range(0, len(display1)):
            display1[i] = str((int(display1[i])+colors[display1color][6])%10)
        for i in range(0, len(display2)):
            display2[i] = str((int(display2[i])+colors[display2color][6])%10)
        for i in range(0, len(display3)):
            display3[i] = str((int(display3[i])+colors[display3color][6])%10)

    print('Display one should be:', FizzBuzzGame(int(''.join(display1))))
    print('Display two should be:', FizzBuzzGame(int(''.join(display2))))
    print('Display three should be:', FizzBuzzGame(int(''.join(display3))))