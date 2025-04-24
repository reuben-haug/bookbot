"""Reads the contents of a text file, printing a report that returns the number of times each word occurs in the text, as well as a count of each time a letter appeared in the text"""

import sys
from stats import count_words, count_letters, count_word_frequency

def read_file(file_path):
    """Read the contents of the file at the given path."""

    with open(file_path) as f:
        return f.read()

def generate_text_report(file_path):
    """Generate a report of word and character counts from a file."""

    file_contents = read_file(file_path)
    word_count = count_words(file_contents)
    char_dict = count_letters(file_contents)
    #word_freq_dict = count_word_frequency(file_contents)

# Sort the dictionaries by highest count
    sorted_char_list = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    #sorted_word_freq_list = sorted(word_freq_dict.items(), key=lambda x:x[1], reverse=True)

    # Header format for the report
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...\n')

    # Word count print
    print(f'----------- Word Count ----------\n')
    print(f'Found {word_count} total words')

    # Step through the character dictionary, print the results
    for char, count in sorted_char_list:
        print(f'{char}: {count}')
    
    # Footer format for the reports
    print(f'============= END ===============')
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    generate_text_report(file_path)