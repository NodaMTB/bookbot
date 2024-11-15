def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    letters = text.lower() 
    character_dict = character_usage(letters)
    
    sorted_count = dict_sort(character_dict)
    for char, count in sorted_count:
        print(f"The '{char}' character was found {count} times")
    

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
   
def get_word_count(text):
    words = text.split()
    return len(words)


def character_usage(letters):
    character_dict = {}
    for letter in letters:
        if letter not in character_dict:
            character_dict[letter] = 1
        else:
            character_dict[letter] += 1
    return character_dict

def sort_on(character_dict):
    return character_dict[1]

def dict_sort(character_dict):
    character_sorted = [(char, count) for char, count in character_dict.items() if char.isalpha()]
    character_sorted.sort(reverse=True, key=sort_on)
    return character_sorted
    





    
    
    

main()