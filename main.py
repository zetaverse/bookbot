from stats import get_num_words, get_num_characters, get_sorted_list

def main():
    num_words = get_num_words("books/frankenstein.txt")
    sorted_list = get_sorted_list("books/frankenstein.txt")
    file_path = "books/frankenstein.txt"

    # Printing the book report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    # printing the character dict list
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()