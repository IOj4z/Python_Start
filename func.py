
def set_register(s):
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()


print(set_register("Hello world"))


