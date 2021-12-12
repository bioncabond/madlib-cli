from sys import exit 
import re, os

file= "../assets/dark_and_stormy_night_template.txt"

print("""
*******Welcome to Madlib*******
  
Rules & Directions: 
  
** 1. You will be prompted with a series of word request.**
These words will be things like:
Name: Somebody..Anybody (ie. Your Name, Your Momma's Name, Pookie from down the street) 
Adjective: Something that describes a noun (ie. big, fast, colorful ) 
Noun: any singular person, place or thing
Plural Noun: anything that you can add an s to represent more than one or collection (ie. pencils, cards, books) 
  
** 2. Your words will appear in the madlib reflecting your choices**
**What does this look like? Good question: 
adjective: big
adjective: colorful
noun: book 
  
**********Madlib Display**********
It was a (adjective: <big>) and (adjective: <colorful>) (noun:<book>).
It was a big and colorful book.
**********************************
""")  

def word_list(words):
    word_array = [] 
    for i in words:
        response = input(f'Please enter a {i}:')
        word_array.append(response)
    return word_array 
    
def read_template(file_path): 
    with open(file_path, 'r') as read_file: 
            text = read_file.read()
            return text 
    # if in file:
    #     raise FileNotFoundError: 
    #         print("Sorry, I can't find that file. {e}")
    

def parse_template(text):
    strip = r"{([\w ',.-]+)}"
    words = tuple(re.findall(strip,text)) 
    text_template = re.sub(strip, '{}',text)
    # print(text_template,words)
    return text_template,words

def merge(text_template,words): 
    return text_template.format(*words)

def save_to_effing_file (final_madlib):
    with open('../written_madlibs/ya_mommas_file.txt', 'w') as written_file: 
            text = written_file.write(final_madlib)

if __name__ == "__main__":
# ##Function Calls/invoke:
    text = read_template(file)
    text_template,words=parse_template(text)
    word_text=word_list(words)
    final_madlib = merge(text_template,word_text)
    save_to_effing_file(final_madlib)
    