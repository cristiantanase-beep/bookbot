import sys
from stats import count_words, count_characters, get_sorted_characters


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
   
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path=sys.argv[1]
    book_text = get_book_text(path)

    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(book_text)
    sorted_chars = get_sorted_characters(char_counts)
   
    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
  


main()
