import unicodedata

blacklist = ['import', 'os', 'system', 'eval', 'exec', '__builtins__']

payload = input()
payload = unicodedata.normalize('NFKC', payload)

for word in blacklist:
    if word in payload:
        print('ban')
        exit()
print(eval(payload, {"__builtins__": {}},{"__builtins__": {}}))