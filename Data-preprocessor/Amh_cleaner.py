from re import split, match
from .AmahricNumber import  Amharic_Numbers
class Cleaner:
    def __init__(self,text):
        self.text=text

    def clean_numbers(self):

        words=split(" ",self.text)
        text=""
        i=0
        for word in words:
            if(match([0-9],word)):
                number=Amharic_Numbers(word)
                if(words[i+1] == "q.m" || words[i+1] == "q/m" ):
                    text=text+" "+number.convert_year()
                else:
                    text=text+" "+number.num_to_word()

            elif(word.__contains__("/") || word.__contains__(".")):



