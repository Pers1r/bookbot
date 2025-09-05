from stats import count_words, count_characters, get_sorted_characters
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    print(f'============ BOOKBOT ============/nAnalyzing book found at {path}...\n----------- Word Count ----------')
    print("Found", count_words(book_text), "total words\n--------- Character Count -------")
    for x in get_sorted_characters(book_text):
        print(x["char"] + ': ' + str(x["num"]))
    print('============= END ===============')


main()