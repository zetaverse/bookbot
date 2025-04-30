def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words_array = file_contents.split()
    word_count = len(words_array)
    result = (f"{word_count} words found in the document.")
    return result


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
    
    return char_dict

def sort_on(dict):
    return dict["count"]

def get_sorted_list(file_path):
    dict = get_num_characters(file_path)

    char_list = []

    for char in dict:
        char_list.append({"char": char, "count": dict[char]})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
