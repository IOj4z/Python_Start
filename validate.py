import re


email = input("Whats your email? ").strip()
# regex = re.search(r'^.+@.+(\.[A-Z|a-z]{2,})$', email, re.IGNORECASE)
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex = re.compile(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}"
                   r"[a-zA-Z-0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
if re.fullmatch(regex, email):
    print("Valid")

else:
    print("Invalid")