from stats import get_num_words
from stats import characters_in_text

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    chars = characters_in_text(text)
    print(chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

