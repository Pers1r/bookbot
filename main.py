from stats import count_words


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(count_words(book_text), "words found in the document")


main()