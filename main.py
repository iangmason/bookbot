def wordcount(file_contents):
    words = []
    words = file_contents.split()
    return words

def lettercount(file):
    letters_counted = {}
    for letter in file:
        if letter not in letters_counted:
            letters_counted[letter] = 1    
        letters_counted[letter] += 1
    return letters_counted
    
def report(counts, words):
    print("--- Report on frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    sorted_count = sorted(counts.items())
    for item in sorted_count:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")
    
    
def main():    
    f = open("./books/frankenstein.txt")
    file_contents = f.read()
    tocount = file_contents.lower()
    words = wordcount(tocount)
    letters_counted = lettercount(tocount)
    report(letters_counted, words)
    
main()