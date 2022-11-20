# def main():
#     print_square(3)
#
#
# def print_square(size):
#     for i in range(size):
#         print_row(size)
#
#
# def print_row(width):
#     print("#" * width)
#
#
# main()

def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * i)


if __name__ == "__main__":
    main()
