x = 75
user_num = 0
cnt = 0

while True:
    user_num = int(input("Number: "))
    cnt += 1
    if user_num == x:
        print(f"you try: {cnt}")
        print(f"good game")
        break
    elif user_num > x:
        print('Height number')
    else:
        print("Lower pls")
