import sys
import re


def main():
    regex = re.compile(r"(\/\s){2,}")
    chars_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "..-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "/",
        "\n": "\n"
    }

    try:
        with open(sys.argv[1]) as f:
            text = f.readlines()
    except:
        print("You did something wrong.")

    new_string = []
    for line in text:
        new_line = ""
        for char in line.strip().upper():
            if (char in chars_dict):
                new_line += chars_dict[char] + " "
        new_line = re.sub(regex, '/ ', new_line)
        new_string.append(new_line)

    new_string = '\n'.join(new_string)
    print(new_string)


if __name__ == '__main__':
    main()