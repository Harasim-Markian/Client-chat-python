alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZЯ' \
          'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
          '1234567890*/'
step = int(1)
while True:
    message = input("Enter a message to code: ").upper()
    resolt = ''

    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + step
        if i in alfavit:
            resolt += alfavit[new_mesto]
        else:
            resolt += i
    print(resolt.lower())
    message1 = input("Enter a message to uncode: ").upper()
    resolt = ''
    for i in message1:
        mesto = alfavit.find(i)
        new_mesto = mesto - step
        if i in alfavit:
            resolt += alfavit[new_mesto]
        else:
            resolt += i
    print(resolt.lower())