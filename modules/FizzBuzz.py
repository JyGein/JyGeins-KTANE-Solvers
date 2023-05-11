def FizzBuzz(number, amount, phrase):
  if number % amount == 0:
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
    booleans = [bool(input('Are there 5 or more batteries? (True or False): '                        ).lower() != 'false'), # Batteries
                bool(input('Are there 3 or more battery holders? (True or False): '                  ).lower() != 'false'), # BatteryHolders
                bool(input('Is there a Serial and Parallel port? (True or False): '                  ).lower() != 'false'), # SerialParallel
                bool(input('Are there 3 letters and 3 digits in the Serial Number? (True or False): ').lower() != 'false'), # SerialNum
                bool(input('Is there a Dvi-D and a Stereo RCA port? (True or False): '               ).lower() != 'false'), # DviStereo
                bool(input('Are there 2 or more strikes? (True or False): '                          ).lower() != 'false')] # Strikes
    display1 = [i for i in display1] # [*display1] Will do the same thing, but keeping it as a list comp will probably be more clear - Taser
    display2 = [i for i in display2]
    display3 = [i for i in display3]
    colors = {'red'   : [1, 7, 3, 4, 2, 6, 3], 
              'green' : [2, 3, 4, 5, 3, 6, 1], 
              'blue'  : [2, 2, 9, 8, 7, 1, 8], 
              'yellow': [5, 4, 2, 8, 9, 2, 3], 
              'white' : [3, 5, 8, 2, 1, 8, 4]}  
    for k in range(0,6): # Since the length of boolens does not change, we don't need to check the length of it, and can just manually put its length.
        if booleans[k]:
            for i in range(0, len(display1)):
                display1[i] = str((int(display1[i])+colors[display1color][k])%10)
            for i in range(0, len(display2)):
                display2[i] = str((int(display2[i])+colors[display2color][k])%10)
            for i in range(0, len(display3)):
                display3[i] = str((int(display3[i])+colors[display3color][k])%10)
    if any(booleans) == False:
        for i in range(0, len(display1)):
            display1[i] = str((int(display1[i])+colors[display1color][6])%10)
        for i in range(0, len(display2)):
            display2[i] = str((int(display2[i])+colors[display2color][6])%10)
        for i in range(0, len(display3)):
            display3[i] = str((int(display3[i])+colors[display3color][6])%10)

    print('Display one should be:',   FizzBuzzGame(int(''.join(display1))))
    print('Display two should be:',   FizzBuzzGame(int(''.join(display2))))
    print('Display three should be:', FizzBuzzGame(int(''.join(display3))))
