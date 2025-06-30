def count_words(book_txt):
    words = book_txt.split()
    return len(words)

def count_chars(text):
    text_lower = text.lower()
    chars = {}
    for char in text_lower:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    char_list = []
    for char in chars:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = chars[char]
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list