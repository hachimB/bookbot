# display_result function prints the the valid letter and there occurence with this format:
# The <valid letter> character was found <occurence> times 
def display_result(l):
    for elem in l:
        print(f"The '{elem['key']}' character was found {elem['value']} times")

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
 
# Word count function returns the number words in the text
def word_count(f_contents):
    count = 0
    arr = f_contents.split()
    for content in arr:
        count += 1
    return count

# The main function
def main():

    path = "books/frankenstein.txt"
    # Let's first the content of the file 
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
    print(f"--- Begin report of {path} ---")
    print(f"{word_count(f_contents)} words found in the document")
    print()
    l = clean_array(dictionary)
    l.sort(reverse=True, key=on_sort)
    display_result(l)
    print("--- End report ---")

# And here we are calling the main function
main()
