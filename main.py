import sys
from stats import word_counter, character_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(path)} total")
    print("--------- Character Count -------")
    character_sorted_list(path)
    print("============= END ===============")


main(sys.argv[1])
