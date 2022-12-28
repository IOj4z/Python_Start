alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", " "]


def data():
    msg = input('Enter word: ')
    number = int(input('Enter number (1-26): '))
    while number > 26 or number == 0:
        number = int(input('Enter correct number (1-26): '))
    datas = (msg, number)
    return datas


def decode(msg, number):
    n_msg = ''
    for x in msg:
        y = alphabet.index(x)
        y = y - number
        if y < 0:
            y = y + 27
        res = alphabet[y]
        n_msg = n_msg + res
    print(n_msg)


def encode(msg, number):
    n_msg = ''
    for x in msg:
        y = alphabet.index(x)
        y = y + number
        if y > 26:
            y = y - 27
        res = alphabet[y]
        n_msg = n_msg + res
    print(n_msg)


def main():
    while True:
        func = ['1) Make a code', '2) Decode a message', '3) Quit', 'Enter your selection: ']
        for x in func:
            print(x)
        num_func = int(input("Choose function: "))
        match num_func:
            case 1:
                (msg, number) = data()
                encode(msg, number)
            case 2:
                (msg, number) = data()
                decode(msg, number)
            case 3:
                print('Good bye!')
                return False
            case _:
                print("Uncorrected")


if __name__ == '__main__':
    main()
