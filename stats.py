# stats.py

import collections

def load_common_words(file_path):
    """Load common words from a file into a set."""
    with open(file_path, 'r') as f:
        common_words = set(word.strip() for word in f)
    return common_words

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