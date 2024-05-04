blacklist = ['import']

payload = input()
for word in blacklist:
    if word in payload:
        print('ban')
        exit()
print(eval(payload))