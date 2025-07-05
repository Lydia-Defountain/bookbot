def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def get_word_count(filepath):
    contents = get_book_text(filepath)
    words = []
    words = contents.split()
    return len(words)

def get_character_count(filepath):
    contents = get_book_text(filepath)
    contents = contents.lower()
    character_count = {}
    for character in contents:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(items):
    return items["num"]
    
def get_sorted_count(filepath):
    character_count = get_character_count(filepath)
    sorting_characters = []
    characters = {}
    for character in character_count:
        sorting_characters += [
            {"char": character,
            "num": character_count[character]}
        ]
    sorting_characters.sort(reverse=True, key=sort_on)
    for i in range(0, len(sorting_characters)):
        if sorting_characters[i]["char"].isalpha():
            characters[(sorting_characters[i]["char"])] = (sorting_characters[i]["num"])
    for char in characters:
        print(f"{char}: {characters[char]}")
            
        