from ciphers import Cipher
import string


class PolybiusSquare(Cipher):
    def __init__(self):
        """Creates a dictionary where keys are alphabet letters and
        digits and values are positions of that letter/diggit
        in the table of 6x6.
        """
        self.characters = string.ascii_uppercase + string.digits
        self.positions = [(x, y) for x in range(1, 7)
                          for y in range(1, 7)]
        self.table = {letter: position for letter, position in
                      zip(self.characters, self.positions)}

    def encrypt(self, text):
        """Takes text and loops through characters finding
        their position in the table and adding it to the list
        Returns the list of positions of characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                pos1, pos2 = self.table[char]
                output.append(str(pos1) + str(pos2))
            except KeyError:
                output.append(char)
            except ValueError:
                output.append(char)
        return " ".join(output)

    def decrypt(self, text):
        """Takes text and splits it in a list.
        Loops through it using elements as positions
        of plaintext character in the table.
        Adds each character to a list.
        Returns the list of characters joined in a
        string.
        """
        output = []
        # Three spaces in a row indicate that there is a whitespace in the
        # message that needs to be preserved and therefore is replaced with '*'
        # so it is not lost by spliting the string and can be recreated.
        if "   " in text:
            text = text.replace("   ", " * ")
        text = text.split()
        print(text)
        for char in text:
            try:
                pos = (int(char[0]), int(char[1]))
                output += [key for key, value in self.table.items() if
                           value == pos]
            except KeyError:
                output.append(char)
            except ValueError:
                output.append(char)
        output = "".join(output)
        return output.replace("*", " ")
