def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main ():
    return (get_book_text("./books/frankenstein.txt"))

def number_of_words():
    words = main().split()
    word_count = len(words)
    return word_count
count = number_of_words()
print(f"Found {count} total words")

