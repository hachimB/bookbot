# Word count function returns the number of words in the text
def word_count(f_contents):
    count = 0
    arr = f_contents.split()
    for content in arr:
        count += 1
    return count

# display_result function prints the the valid letter and there occurence with this format:
# The <valid letter> character was found <occurence> times 
def display_result(l):
    for elem in l:
        print(f"{elem['key']}: {elem['value']}")