
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def word_counter(filepath):
    file_text = get_book_text(filepath)
    split_words = file_text.split()
    return f"Found {len(split_words)} total words"


def character_counter(filepath):
    file_text = get_book_text(filepath)
    lower_case_file_text = file_text.lower()
    letter_count_dict = {}
    for letter in lower_case_file_text:
        if letter not in letter_count_dict:
            letter_count_dict[letter] = 1
        else:
            letter_count_dict[letter] += 1
    return letter_count_dict


#def sort_on(items):
#    return items["num"]

def character_sorted_list(filepath):
    content_list = character_counter(filepath)
    sorted_list = sorted(
        content_list.items(),
        key=lambda item: item[1],
        reverse=True
    )
    for entry, value in sorted_list:
        if entry.isalpha():
            print(f"{entry}: {value}")
        else:
            pass
