import sys

from stats import count_words
from stats import count_characters
from stats import sort_counts

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main(filepath):
    book = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    for character in sort_counts(count_characters(book)):
        key = next(iter(character))
        if key.isalpha():
            value = character[key]
            print(f"{key}: {value}")
    print("============= END ===============")
 
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
