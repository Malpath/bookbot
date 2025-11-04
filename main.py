import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import characters_in_text
from stats import sort_characters

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = characters_in_text(text)
    for i in sort_characters(chars):
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

