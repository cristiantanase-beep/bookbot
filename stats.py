def count_words(book_text):
    words = book_text.split()
    return len(words)


def count_characters(book_text):
    characters = {}

    for char in book_text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters


def sort_on(item):
    return item["num"]


def get_sorted_characters(character_counts):
    items = []

    for ch, count in character_counts.items():
        items.append({"char": ch, "num": count})

    # sort greatest -> least by "num"
    items.sort(key=sort_on, reverse=True)

    return items