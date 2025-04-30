def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words_array = file_contents.split()
    word_count = len(words_array)
    print(f"{word_count} words found in the document.")


def get_num_characters(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.lower()
    char_list = list(words)

    char_dict = {}

    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    print(char_dict)


