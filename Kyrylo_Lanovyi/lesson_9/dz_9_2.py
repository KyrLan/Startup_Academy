import string


class TextProcessor:
    def __init__(self, _punkt):
        self._punkt = _punkt

    def get_clean_string(self, get_string):
        if self._punkt == True:
            cleaned_string = get_string.translate(str.maketrans('', '', string.punctuation))
        else:
            cleaned_string = self._punkt
        return cleaned_string

    def __is_punktiatian(self):
        if any(n in string.punctuation for n in get_string):
            self._punkt = True
        else:
            self._punkt = False
        return self._punkt


class TextLoader:

    def __init__(self, __clean_string):
        self.__text_processor = TextProcessor()
        self.__clean_string = __clean_string

    def set_clean_text(self, get_string):
        self.__clean_string = self.__text_processor.get_clean_string(get_string)

    @property
    def message(self):
        print("You cleaned text - " + str(self.__clean_string))

class DataInterface:

    def __init__(self):
        self._textloader = TextLoader()

    def process_texts(self, string_list):
        for i in string_list:
            self._textloader.set_clean_text(i)
            return i
