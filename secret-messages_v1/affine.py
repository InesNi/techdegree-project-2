import string
from ciphers import Cipher


class Affine(Cipher):
    def __init__(self, num1, num2):
        """Takes instance and two numbers.
        First number(num1) has to be a coprime of 26.
        It creates a dictionary where keys are alphabet letters
        and values are ciphertext value for the given letter.
        Ciphertext value of each letter is calculated by formula:
        E(x) = (ax + b) mod 26
        where 26 is the size of the alphabet, and 'a' and 'b' are key
        of the cipher provided by the arguments num1 and num2.
        """
        self.num1 = num1
        self.num2 = num2
        self.table = {
            chr(num + 65): chr(((num1 * num + num2) % 26)+65)
            for num in range(26)
        }

    def encrypt(self, text):
        """Takes text and loops through characters finding
        their encrypted version in the dictionary created in
        initialisation of class, which then appends to a list.
        Returns the list of encrypted characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                output.append(self.table[char])
            except ValueError:
                output.append(char)
            except KeyError:
                output.append(char)
        return "".join(output)

    def decrypt(self, text):
        """Takes text and loops through characters finding
        their decrypted version in the dictionary created in
        initialisation of the class, which then appends to a list.
        Returns the list of decrypted characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            output += [key for key, value in self.table.items()
                       if char == value]
            if char not in string.ascii_uppercase:
                output.append(char)

        return "".join(output)
