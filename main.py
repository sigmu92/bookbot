import sys
from stats import count_words, count_chars, sort_chars

def get_book_test(path):
    """
    Test function to get a book from the given path.
    """
    try:
        with open(path, 'r') as file:
            book_content = file.read()
        return book_content
    except FileNotFoundError:
        return "Book not found at the specified path."
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_test(file_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_chars = sort_chars(char_count)
    print("============= BOOKBOT =============")
    print(f"Analysing book found at {file_path}")
    print("------------ Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("=============== END ===============")
        
main()