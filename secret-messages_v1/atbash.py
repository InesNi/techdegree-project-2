import string
from ciphers import Cipher


class Atbash(Cipher):
    """Creates two strings, one is the uppercase
    letters of the alphabet in order, and the other
    is alphabet reversed
    """
    def __init__(self):
        self.plain = string.ascii_uppercase
        self.cipher = string.ascii_uppercase[::-1]

    def encrypt(self, text):
        """Takes text and loops through characters finding
        their index in the alphabet string and appending the
        letter with the same index in reversed alphabet string
        to a list.
        Returns the list of encrypted characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.plain.index(char)
            except ValueError:
                output.append(char)
            except KeyError:
                output.append(char)
            else:
                output.append(self.cipher[index])
        return "".join(output)

    def decrypt(self, text):
        """Takes text and loops through characters finding
        their index in the reversed alphabet string and appending the
        letter with the same index in the alphabet string
        to a list.
        Returns the list of decrypted characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.cipher.index(char)
            except ValueError:
                output.append(char)
            except KeyError:
                output.append(char)
            else:
                output.append(self.plain[index])

        return "".join(output)
