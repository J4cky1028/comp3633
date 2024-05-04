import unicodedata

blacklist = ['import', 'os', 'system', 'eval', 'exec', 'lambda',
             'help', 'dict', 'dir', 'input', 'locals', 'compile',
             'bool', 'any', 'ascii', '__builtins__', '__class__',
             '[', ']']

def pyjail():
    print('Welcome to HKUST!')
    print('What do you want to do now?')
    print('What? you want to escape?!!i!!11!l!!11!')
    method = input('How?\n')
    method = unicodedata.normalize('NFKC', method)
    for word in blacklist:
        if word in method:
            print('You can\'t escape from HKUST, you GG.')
            return
    eval(method, {"__builtins__": {"print": print}},{"__builtins__": {}})
