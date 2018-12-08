import string

from ciphers import Cipher


class Keyword(Cipher):
    def __init__(self, keyword=""):
        """Takes a string as a keyword agrument.
        Creates a string to be used as ciphertext by
        using a keyword string and adding the alphabet
        to it without the letters that are present in the keyword.
        Creates another string that is alphabet
        letters in order.
        """
        if " " in keyword:
            keyword = keyword.replace(" ", "")
        self.keyword = keyword.upper()
        encr_alpha = self.keyword + string.ascii_uppercase
        result = []
        for char in encr_alpha:
            if char not in result:
                result.append(char)
        self.encr_alpha = "".join(result)
        self.decr_alpha = string.ascii_uppercase

    def encrypt(self, text):
        """Takes text and loops through characters finding
        their index in the alphabet string and appending the
        letter with the same index in ciphertext string
        to a list.
        Returns the list of encrypted characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.decr_alpha.index(char)
            except ValueError:
                output.append(char)
            except KeyError:
                output.append(char)
            else:
                output.append(self.encr_alpha[index])
        return "".join(output)

    def decrypt(self, text):
        """Takes text and loops through characters finding
        their index in the ciphertext string and appending the
        letter with the same index in alphabet string
        to a list.
        Returns the list of decrypted characters joined in a
        string.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.encr_alpha.index(char)
            except ValueError:
                output.append(char)
            except KeyError:
                output.append(char)
            else:
                output.append(self.decr_alpha[index])

        return "".join(output)
