from stats import get_character_count, get_sorted_character_count, get_word_count


def get_book_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf8") as fp:
        return fp.read()


def main(file_path: str) -> None:
    print("============== BOOKBOT ==============")
    print(f"Analyzing book found at {path}...")
    print("------------- Word Count ------------")
    text = get_book_text(file_path)
    wc = get_word_count(text)
    print(f"Found {wc} total words")

    print("----------- Character Count ---------")
    char_count = get_character_count(text)
    for character in get_sorted_character_count(char_count):
        if character["char"].isalpha():
            print(character["char"], character["num"], sep=": ")

    print("================ END ================")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        path = sys.argv[1]
        main(path)
    else:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
