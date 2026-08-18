print("Hello regex!!")
import re
text="this is some regular text."

pattern=r'this is some regular text\.'
#searches for a match anywhere in the string
match=re.search(pattern,text)
if match is not None:
    print(f"Match found:{match}")

text1="The big red cat ate the fat rat"
pattern1=r'[A-Za-z]{3}'
#findall() returns a list of all matches
match1=re.findall(pattern1,text1)
if match1:
    print(f"The match are:{match1}")
story="I went to the park and I saw my friend and My friends dog was there and That was good"
and_pattern=re.compile(r'\sand')
# .split() splits the text at the argument given
print(and_pattern.split(story))
# .sub() allows string manipulation 
print(and_pattern.sub(".",story))

#match returns a match object at the start of the string otherwise ==>returns None

string="123     apples"
pattern2=r'\d+'
match2=re.match(pattern2,string)
if not match2:
    print("The match is not at the start")
else:
    print(f'The match is;{match2}')
    # fullmatch() returns a match object if everything in the string matches thr pattern
pattern3=r'\d+\s+\w+'
match3=re.fullmatch(pattern3,string)
if not match3:
    print("Everything didnt match")
else:
    print(f"I found a match:{match3}")