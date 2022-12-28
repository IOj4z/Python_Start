import random


def com_col():
    colors = ['r', 'b', 'o', 'y', 'p', 'g', 'w']
    comp1 = random.choice(colors)
    comp2 = random.choice(colors)
    comp3 = random.choice(colors)
    comp4 = random.choice(colors)
    result = (comp1, comp2, comp3, comp4)
    return result


def get_data(comp1, comp2, comp3, comp4):

    print("The colours are: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (g)reen and (w)hite.")
    retry = True
    while retry:
        ch1 = input('Enter 1 name of color: ').lower()

        if len(ch1) != 1:
            print('Incorrect enter')
        else:
            retry = False
    retry = True
    while retry:
        ch2 = input('Enter 2 name of color: ').lower()
        if len(ch2) != 1:
            print('Incorrect enter')
        else:
            retry = False
    retry = True
    while retry:
        ch3 = input('Enter 3 name of color: ').lower()
        if len(ch3) != 1:
            print('Incorrect enter')
        else:
            retry = False
    retry = True
    while retry:
        ch4 = input('Enter 4 name of color: ').lower()
        if len(ch4) != 1:
            print('Incorrect enter')
        else:
            retry = False

    correct = 0
    wrong = 0

    if comp1 == ch1:
        correct = correct + 1
    elif comp1 == ch2 or comp1 == ch3 or comp1 == ch4:
        wrong = wrong + 1

    if comp2 == ch2:
        correct = correct + 1
    elif comp2 == ch1 or comp2 == ch3 or comp2 == ch4:
        wrong = wrong + 1

    if comp3 == ch3:
        correct = correct + 1
    elif comp3 == ch1 or comp3 == ch2 or comp3 == ch4:
        wrong = wrong + 1

    if comp4 == ch4:
        correct = correct + 1
    elif comp4 == ch1 or comp4 == ch2 or comp4 == ch3:
        wrong = wrong + 1

    print("Correct colour in the correct place: ", correct)
    print("Correct colour but in the wrong place: ", wrong)
    return [correct, wrong]


def main():
    (comp1, comp2, comp3, comp4) = com_col()
    score = 0
    while True:
        (correct, wrong) = get_data(comp1, comp2, comp3, comp4)
        print((correct, wrong) )
        score = score + 1
        if correct == 4:
            return False
    print('You win!')
    print('You took', score, 'guesses')


if __name__ == '__main__':
    main()
