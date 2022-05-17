import sys
import codecs


def load_textfile(filename: str):
    try:
        with codecs.open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
    except:
        print("Couldn't read the file!")
        sys.exit(1)

    return content


class FirstWords:
    def __init__(self, filename: str):
        self.text = load_textfile(filename)
        self.__get_rid_of_illegal_chars__()
        self.text = self.text[411:7599].split()

    def __get_rid_of_illegal_chars__(self):
        illegal_chars = "()'-:,.?!;—"

        for char in illegal_chars:
            self.text = self.text.replace(char, "")

    def get(self, number_of_words):
        return self.text[:number_of_words]
