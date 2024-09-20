def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_arr_sorted = dict_to_report(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_arr_sorted:
        if item["name"].isalpha():
            print(f"The '{item['name']}' character was found {item['num']} times")
    
    print("--- End report ---")

def dict_to_report(dict):
    result = []
    for key, value in dict.items():
        result.append({"name": key, "num": value})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()