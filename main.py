#read the contents of frankenstein.txt
with open("./books/frankenstein.txt") as f:

    #contents of the file as a string
    file_contents = f.read()
    
    #return the number of words
    def count_words(file_contents):
        words = file_contents.split()
        return len(words)

    #return the number of characters, ignoring case
    def count_letters(file_contents):
        #initialize an empty return dictionary
        letter_dict = {}
        for char in file_contents:
            #convert to lowercase
            lower_char = char.lower()
            #only alphanumeric characters
            if char.isalpha() == True:
                if lower_char in letter_dict:
                    letter_dict[lower_char] += 1
                else:
                    letter_dict[lower_char] = 1
        return letter_dict
    
    def text_report():
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