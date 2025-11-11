
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