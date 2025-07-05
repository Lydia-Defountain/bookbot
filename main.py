from stats import get_word_count, get_book_text, get_sorted_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(sys.argv[1])} total words")
    print("--------- Character Count -------")
    get_sorted_count(sys.argv[1])
    print("============= END ===============")

main()