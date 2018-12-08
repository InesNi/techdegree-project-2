import string


class OnePad:
    def __init__(self, pad):
        """Takes a pad number.
        Creates a dictionary with keys as alphabet letters
        and values as index of the key letter in the alphabet
        """
        self.pad = pad
        self.alpha_num = {
            letter: number for number, letter in
            enumerate(string.ascii_uppercase)
        }

    def encrypt(self, message):
        """Takes text and loops through characters finding
        their index value and adding it to the corresponding
        pad character on the same index using modular addition.
        Takes given value as index of ciphertext character
        that then appends to a list.
        Returns the list of encrypted characters joined in a
        string.
        """
        result = []
        message = message.upper()
        index = 0
        for char in message:
            try:
                num_ciph = ((int(self.alpha_num[char]) +
                             int(self.pad[index])) % 26)
            except ValueError:
                result.append(char)
            except KeyError:
                result.append(char)
            else:
                result += [key for key, value in
                           self.alpha_num.items() if num_ciph ==
                           value]
            if index < len(self.pad) - 1:
                index += 1
            else:
                index = 0
        return "".join(result)

    def decrypt(self, message):
        """Takes text and loops through characters finding
        their index value and substracts the corresponding
        pad character on the same index from it using modular addition.
        Takes given value as index of decrypted character
        that then appends to a list.
        Returns the list of decrypted characters joined in a
        string.
        """
        result = []
        message = message.upper()
        index = 0
        for char in message:
            try:
                num_deci = ((int(self.alpha_num[char]) -
                             int(self.pad[index])) % 26)
            except ValueError:
                result.append(char)
            except KeyError:
                result.append(char)
            else:
                result += [key for key, value in
                           self.alpha_num.items() if num_deci ==
                           value]
            if index < len(self.pad) - 1:
                index += 1
            else:
                index = 0
        return "".join(result)
