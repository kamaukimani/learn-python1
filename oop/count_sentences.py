print("Let's count some sentences")
class MyString:
    def __init__(self,value=""):
        self._value=value  #the underscore tells programmers the value shouldnt be accessed directly
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,string_val):
        if type(stringVal == str):
            self._value=string_val
        else:
            raise TypeError("The value must be a string")
    @value.deleter
    def value(self):
        raise  AttributeError(
            "The value can not be deleted"
        )
    def is_sentence(self):
        return self_value.endswith(".")
    def is_question(self):
        return self._value.endswith("?")
    def is_exclamation(self):
        return self._value.endswith("!")
    def count_sentences(self):
        value=self.value
        for punc in ["!","?"]:
            value=value.replace(punc,".")

        sentences=[s for s in value.split(".") if s]
        print(sentences)

        length=len(sentences)
        print(f"The number of sentences is: {length}")
        return length

string=MyString("This is a string! It has three sentences. Right?")
string.count_sentences()
del string.value