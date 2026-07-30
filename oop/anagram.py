print("Hello!!!Welcome to the Anagram class")
#print(sorted("hello"))
class Anagram:
    def __init__(self,word):
        self.word=word
    def match(self,word_list):
        matches=[]
        
        for word in word_list:
            if sorted(word)==sorted(self.word):
                print(f"commparing: {word} with: {self.word}")
                matches.append(word)
        return matches
anagram=Anagram("enlist")
matching=anagram.match(["hello","listen","come","stenli","setnil"])
print(matching)
