"""
Prompt the user to enter a name. Print the length of the name.
"""

# name = input("Enter your name: ")
# print(len(name))

"""
Prompt the user to enter a first name,
and then the last name. Concatenate them by separating 
them with a space, then output the full name and its
length.
"""

# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# userName = firstName + " " + lastName
# print("Hello,", userName, len(userName))

"""
Offer the user
enter the first line of some poem, output the length of the line. 
Request start and end position and output only this one
part of a string (don't forget that
in python index numbering
starts at 0, not 1).
"""
# poem = input("Enter first row poem: ")
# print(poem[-1])

"""
Prompt the user to enter a name. Print it in upper case.
"""
# name = input("Enter your name: ")
# print(name.upper())
# print(name.capitalize())

"""
Prompt the user to enter a name. If the length of the name
less than 5 characters, prompt to enter the last name, connect
them (without spaces) and print the full name in upper case.
If the name is 5 or more characters long, print
name in lower case.
"""
# firstName = input("Enter your name: ")
# if len(firstName) < 5:
#     lastName = input("Enter your last name: ")
#     res = firstName+lastName
#     print(res.upper())
# elif len(firstName) >= 5:
#     print(firstName.lower())

"""
In the pig Latin cipher, the initial consonant
the letter of the word is moved to the end of the word, 
and the suffix "ay" is added to it. If a word begins with a vowel, 
the suffix "way" is simply added to it. For example, 
pig becomes igpay, banana becomes ananabay,
and aardvark is in aardvarkway. Write a program
which prompts the user to enter a word and converts it to pig Latin. Follow that
so that the new word is displayed in lower case.
"""
# consonants = ["Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ",
#               "б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
# vowels = ['А', 'И', 'О', 'У', 'Ы', 'Э', 'а', 'и', 'о', 'у', 'ы', 'э']
# suffix = ['ay', 'way']
word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]

if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"

print(newword.lower())
