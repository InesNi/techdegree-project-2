import os
import secrets
import string
from affine import Affine
from atbash import Atbash
from caesar import Caesar
from keywords import Keyword
from one_pad import OnePad
from polybius_square import PolybiusSquare


def runcrypt(cipher, operation, text):
    """Takes a cipher type, operation and text
    and then runs the operation method of the cipher
    class on the given text.
    Prompts the user for additional information if needed
    for the chosen cipher.
    It encrypts or decrypts text with a chosen cipher
    """
    if cipher == 'Keyword':
        word = input("Enter the keyword: ")
        key = Keyword(keyword=word)

    elif cipher == 'Affine':
        num1 = int(input("Enter the first number(coprime of 26): "))
        num2 = int(input("Enter the second number: "))
        key = Affine(num1, num2)

    elif cipher == 'Atbash':
        key = Atbash()
    elif cipher == 'Caesar':
        key = Caesar()
    elif cipher == 'PolybiusSquare':
        key = PolybiusSquare()

    if operation == 'encrypt':
        result = key.encrypt(text)
    elif operation == 'decrypt':
        result = key.decrypt(text)
    return result


def five_block(iterable, num=5):
    """Takes an iterable and a key argument num which is by default 5.
    Replaces whitespace from iterable with an asterisk and aranges
    it in a string made out of even sized blocks of characters.
    Lenght of the block is set by the key argument num.
    If the iterable lenght is not devidable in the num sized blocks,
    random punctuation characters are used for padding.
    """
    if " " in iterable:
            iterable = iterable.replace(" ", "*")
    block_lists = [iterable[ind: ind + num] for ind
                   in range(0, len(iterable), num)]
    punct = string.punctuation.replace("*", "")
    while len(block_lists[-1]) < num:
        block_lists[-1] += secrets.choice(punct)
    block_str = ["".join(block) for block in block_lists.copy()]
    return " ".join(block_str)


def clear():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_code():
    """Executes a loop in which a user is shown a menu of
    of operations and prompted to choose either to encrypt
    or decrypt text as well as to choose a cipher from the
    available ciphers.
    Prompts the user for all information needed to execute
    operation using the chosen cipher and then executes.
    Uses One pad cipher to additionaly secure data as well as
    aranging output in 5 block character string.
    """
    while True:
        clear()
        operation = input("Available operations are:\n\n"
                          "-encryption\n"
                          "-decription\n\n"
                          "Would you like to encrypt"
                          " or decrypt?  ").lower()
        while operation not in {"encrypt", "decrypt"}:
            operation = input("Please enter 'encrypt' for encryption "
                              "and 'decrypt' for decryption:  ").lower()
        cipher = input("Available ciphers are:\n\n"
                       "Caesar\n"
                       "Atbash\n"
                       "Affine\n"
                       "Keyword\n"
                       "Polybius Square\n\n"
                       "Which cipher would you like to use?  ").title()
        while cipher.lower() not in {"caesar",
                                     "atbash",
                                     "affine",
                                     "keyword",
                                     "polybius square"}:
            cipher = input("Please enter the name "
                           "of the cipher you wish to use:  ").title()
        if " " in cipher:
            cipher = cipher.replace(" ", "")

        text = input("Enter your message: ")
        pad = input("Enter the pad number: ")

        if operation == "encrypt":
            message = OnePad(pad)
            message = message.encrypt(text)
            result = runcrypt(cipher, operation, message)
            result = five_block(result)
        elif operation == "decrypt":
            text = text.replace(" ", "")
            punct = string.punctuation.replace("*", "")
            text = text.replace("*", " ")
            text = [char for char in text if char not in
                    punct]
            text = "".join(text)
            message = runcrypt(cipher, operation, text)
            result = OnePad(pad)
            result = result.decrypt(message)

        print("Here is your message: {}".format(result))
        repeat = input("\n\n Would you like to encrypt/decrypt"
                       " something else? y/n  ")
        while repeat not in {"y", "n"}:
            repeat = input("Please enter y to continue and n to exit: ")
        if repeat.lower() == 'n':
            break
        elif repeat.lower() == 'y':
            continue

if __name__ == '__main__':
    main_code()
