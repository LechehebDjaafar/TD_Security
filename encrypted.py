from click import clear


def get_word_encrypted(key, word_not_encrypted):

    car = 'abcdefghijklmnopqrstuvwxyz'
    word_encrypted = ""
    i = 0
    z = 0
    for x in range(len(word_not_encrypted)):
        if i == (len(key)):
            i = 0
        add = car.index(key[i])
        start = car.index(word_not_encrypted[x])+add
        if start > 25:
            z = 0
            for y in range(start):
                z += 1
                if z > 25:
                    z = 0
            word_encrypted += car[z]
        else:
            word_encrypted += car[start]
        i += 1
    return word_encrypted

def get_word_not_encrypted(key, word_encrypted):
    car = 'abcdefghijklmnopqrstuvwxyz'
    z = 0
    word_not_encrypted = ''
    for x in range(len(word_encrypted)):
        if z > len(key)-1:
            z = 0
        reel1 = car.index(key[z])
        z += 1
        reel2 = car.index(word_encrypted[x])
        if reel1 < reel2:
            num = reel2-reel1
            word_not_encrypted += car[num]
        else:
            num = reel2-reel1
            word_not_encrypted += car[num]
    return word_not_encrypted

def get_key(word_not_encrypted, word_encode):
    car = 'abcdefghijklmnopqrstuvwxyz'
    key = ''
    for x in range(len(word_not_encrypted)):
        reel1 = car.index(word_not_encrypted[x])
        reel2 = car.index(word_encode[x])
        if reel1 < reel2:
            num = reel2-reel1
            key += car[num]
        else:
            num = reel2-reel1
            key += car[num]
    return key

def parameter(word, key):
    if word.count(" ") > 0 or key.count(" ") > 0 or len(key) > len(word):
        return 0
    for x in word:
        if x in '0123456789':
            return 0
    for x in key:
        if x in '0123456789':
            return 0
    return 1

def switch():
    try:
        num = int(input("Enter Number Choose : "))
    except:
        print("ERROR Pleas Enter Numbers 1 or 2 or 3")
        quit()
    if num < 0 or num > 3:
        print("ERROR Pleas Enter Numbers 1 or 2 or 3")
        quit()
    return num

def main():
    clear()
    Q = '''Choose one of the existing options
    -> Encrypt text with a Key ->(1)
    -> Decrypt text with a Key ->(2)
    -> Discover the Key ->(3)'''
    print(Q)
    num = switch()
    if num == 1:
        word = input("Enter Your Encrypt text : ").lower()
        key = input("Enter Your key : ").lower()
        if parameter(word, key) == 0:
            print('Encrypt text or key Not correct Pleas agin')
        else:
            word_encrypted = get_word_encrypted(key, word)
            print(f"Encrypt text<{word}> is {word_encrypted}")
    elif num == 2:
        word = input("Enter Your Decrypt text : ").lower()
        key = input("Enter Your key : ").lower()
        if parameter(word, key) == 0:
            print('Decrypt text or key Not correct Pleas agin')
        else:
            word_encrypted = get_word_not_encrypted(key, word)
            print(f"Decrypt text<{word}> is {word_encrypted}")
    elif num == 3:
        word = input("Enter Your Encrypt text : ").lower()
        key = input("Enter Your Decrypt text : ").lower()
        if parameter(word, key) == 0:
            print('Encrypt text or Decrypt text Not correct Pleas agin')
        else:
            word_encrypted = get_key(word, key)
            print(f"Kay Encrypt text<{word}> is {word_encrypted}")

main()
