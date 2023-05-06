import importlib
import sys

sys.path.insert(0, r'C:\Users\jygei\Desktop\ktane autosolvers\code\modules')
module = input('What module?: ')
modulename = importlib.import_module(module)
print(modulename.run())

os.system("pause")