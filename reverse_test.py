### reverse_test

"""
x is a string representing a book of text. The pages are separatd by \b. The lines by \n. 

Write a function that reverses the
- order of pages
- order of lines in each page
- order of words in each line
- don't reverse the characters in each word

Sample string:
x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
"""

def reverse_everything(s):
    pages_ = []
    pages = s.split("\b")
    for page in pages:
        lines = page.split("\n")
        lines_ = []
        for line in lines:
            words = line.split(" ")[::-1]
            lines_.append(" ".join(words))
        lines_ = lines_[::-1]
        lines_ = "\n".join(lines_)
        pages_.append(lines_)
    pages_ = pages_[::-1]
    pages_ = "\b".join(pages_)    
    return pages_
   

x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
print(reverse_everything(x))
