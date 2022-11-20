import sys

# if len(sys.argv) < 2:
#     # print("Too few arguments")
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     # print("Too many arguments")
#     sys.exit("Too many arguments")
# else:
#     print("hello, my name is ", sys.argv[1])

if len(sys.argv) < 2:
    # print("Too few arguments")
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)