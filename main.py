import sys
from stats import word_count
from stats import display_result


# This function will return a list with dictionaries of valid letters and their occurences
def clean_array(d):
    l = []
    for k in d:
        if k.isalpha():
            l.append({"key": k, "value": d[k]})
    return l

# This function will help us for sorting an array(list)
def on_sort(d):
  return d["value"]

# char count function returns a dictionary which contains every single character with his occurence
def char_count(f_contents):
    dictionary = {}
    n = 1
    for k in f_contents:
        if k not in dictionary:
            dictionary[k] = n
        else:
            dictionary[k] += 1
    return dictionary
 

# The main function
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    # Let's first read the content of the file 
    with open(path) as f:
        f_contents = f.read()

    # let's print the content of the file to the console
    # print(f_contents)

    #Let's count the number of words in the book
    # print(word_count(f_contents))

    # let's count the number of occurence of every character
    lowercase = f_contents.lower()
    dictionary = char_count(lowercase)
    # print(dictionary)

    # Final output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(f_contents)} total words")
    print("--------- Character Count -------")
    l = clean_array(dictionary)
    l.sort(reverse=True, key=on_sort)
    display_result(l)
    print("============= END ===============")

# And here we are calling the main function
main()
