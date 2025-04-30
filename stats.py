def get_num_words(file_path):
    # Opens the file and reads its contents
    with open(file_path) as f:
        file_contents = f.read()
    # Splits the contents into words and counts them
    words_array = file_contents.split()
    word_count = len(words_array)
    # Returns a formatted string with the total word count
    result = (f"Found {word_count} total words.")
    return result


def get_num_characters(file_path):
    # Opens the file and reads its contents
    with open(file_path) as f:
        file_contents = f.read()
    # Converts the contents to lowercase and creates a list of characters
    words = file_contents.lower()
    char_list = list(words)

    # Initializes a dictionary to store character counts
    char_dict = {}

    # Iterates through each character and counts occurrences
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    # Returns the dictionary of character counts
    return char_dict

def sort_on(dict):
    # Helper function to extract the "count" key for sorting
    return dict["count"]

def get_sorted_list(file_path):
    # Gets the character count dictionary from the file
    dict = get_num_characters(file_path)

    # Converts the dictionary into a list of dictionaries with "char" and "count" keys
    char_list = []
    for char in dict:
        char_list.append({"char": char, "count": dict[char]})
    
    # Sorts the list in descending order based on the "count" key
    # Python's built-in sort function is used with a custom key which takes in the helper function and applies it to each dict in the list and then sorts it.
    char_list.sort(reverse=True, key=sort_on)

    # Returns the sorted list of characters and their counts
    return char_list
