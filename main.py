"""Reads the contents of a text file, printing a report that returns the number of times each word occurs in the text, as well as a count of each time a letter appeared in the text"""
#Required imports
import collections

#read the contents of frankenstein.txt
with open("./books/frankenstein.txt") as f:

    #contents of the file as a string
    file_contents = f.read()

    def count_words(file_contents):
        """return the number of words"""

        words = file_contents.split()
        return len(words)
    
    def count_letters(file_contents):
        """return the number of alphabetical characters, ignoring case"""

        #only count lowercase alphabetical characters
        processed_file_contents = [char.lower() for char in file_contents if char.isalpha()]

        #create a Counter object to tally
        counter = collections.Counter(processed_file_contents)

        #flattern into a regular dictionary
        return dict(counter)
    
    def text_report():
        """Calls word_count & char_dict functions, printing the results"""

        #get the word count dictionary
        word_count = count_words(file_contents)

        #get the character count dictionary
        char_dict = count_letters(file_contents)

        #header format for the book content report
        print(f'--- Begin report of {f.name} ---\n')
        print(f'{word_count} words found in the document\n')

        #sort the dictionary by highest character count
        sorted_char_list = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)

        #step through the character dictionary & print the formatted results for each character
        for entry in sorted_char_list:
            (char, count) = entry
            print(f'The "{char}" character was found {count} times')

        #footer format for the book content report
        print(f'\n--- End report ---')
        
text_report()