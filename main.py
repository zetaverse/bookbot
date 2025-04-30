import sys
from stats import get_num_words, get_num_characters, get_sorted_list

def main():
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit if no file path is provided
    else:
        file_path = sys.argv[1]  # Get the file path from the command-line argument

    # Get the word count and sorted character count list
    num_words = get_num_words(file_path)
    sorted_list = get_sorted_list(file_path)

    # Printing the book report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(num_words)  # Print the total word count
    print("--------- Character Count -------")
    # Print the character counts, filtering only alphabetic characters
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

# Entry point of the program
main()