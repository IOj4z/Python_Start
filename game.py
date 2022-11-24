import random

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
    user_num = int(input("Number: "))
    cnt += 1
    if user_num == x:
        print(f"you try: {cnt}")
        if input('Wanna play again? "y|n":') == 'y':
            x = random.randint(1, 100)
            cnt = 0
        else:
            print(f"good game")
            break
    elif user_num > x:
        print('Height number')
    else:
        print("Low number")
