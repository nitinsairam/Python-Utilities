'''
Program to count most frequent word in any text file

'''

def most_freq_word():
    name = raw_input("Enter file:")         # Enter your file path here
    if len(name) < 1 : name = "Give exact file path with file name"            # Default file name can be provided here
    handle = open(name)             # file handler pointing to specific file
    counts = {}             # Python Dictionary named counts to count the specific words 
    list_words = []             # Python List to have the specific words in the list
    big_num = None              # Most frequent word's count variable initialization
    big_word = None             # Most frequent  word in the file
    for line in handle:
        if not line.startswith('put your exact filtering string here '):            # if you want to filter out any specific line  
            continue
        else:
            words = line.split()            # Splitting the desired line into single word
            list_words.append(words[1])             # Appending each word into Python list of word

    for items in list_words:
        counts[items] = counts.get(items,0)+1           # adding count value to every key in the dictionary
   
  
    for word,count in counts.items():       # Main logic for finding out most frequent word and its count
        if big_num is None or big_num < count:  
            big_num = count
            big_word = word
    print "most frequent word is  '",big_word,"' and it's frequency is '",big_num,"'"
    
if __name__ == "__main__":
    most_freq_word()
