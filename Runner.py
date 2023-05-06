import importlib

module = input('What module?: ')
modulemod = importlib.import_module('{}'.format(module))

print(modulemod.run())