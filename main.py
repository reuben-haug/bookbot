"""Reads the contents of a text file, printing a report that returns the number of times each word occurs in the text, as well as a count of each time a letter appeared in the text"""

import collections

def read_file(file_path):
    """Read the contents of the file at the given path."""

    with open(file_path) as f:
        return f.read()
    
def load_common_words(file_path):
    """Load common words from a file into a set."""
    with open(file_path, 'r') as f:
        common_words = set(word.strip() for word in f)
    return common_words

# Usage
common_words = load_common_words('common_words.txt')

def count_words(file_contents):
    """Return the number of words in the text."""

    words = file_contents.split()
    return len(words)
    
def count_letters(file_contents):
    """Tally & return the number of alphabetical characters, ignoring case."""

    processed_file_contents = [char.lower() for char in file_contents if char.isalpha()]
    counter = collections.Counter(processed_file_contents)
    return dict(counter)

def count_word_frequency(file_contents):
    """Count the frequency of each word in the text, excluding common words."""

    words = file_contents.lower().split()
    words = [word for word in words if word not in common_words]
    counter = collections.Counter(words)

    # Filter the counter dictionary to only include words that were found more than once
    counter = {word: count for word, count in counter.items() if count > 1}
    
    return dict(counter)

def generate_text_report(file_path):
    """Generate a report of word and character counts from a file."""

    file_contents = read_file(file_path)
    word_count = count_words(file_contents)
    char_dict = count_letters(file_contents)
    word_freq_dict = count_word_frequency(file_contents)

# Sort the dictionaries by highest count
    sorted_char_list = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_word_freq_list = sorted(word_freq_dict.items(), key=lambda x:x[1], reverse=True)

    # Header format for the report
    print(f'--- Begin report of {file_path} ---\n')
    print(f'{word_count} words found in the document.\n')

    # Step through the character dictionary, print the results
    for char, count in sorted_char_list:
        print(f'The "{char}" character was found {count} times.')

    # Step through the word frequency dictionary, print the results
    for word, freq in sorted_word_freq_list:
        print(f'The word "{word}" was found {freq} times.')
    
    # Footer format for the reports
    print(f'\n--- End report ---')
        
if __name__ == "__main__":
    file_path = "./books/frankenstein.txt"
    generate_text_report(file_path)