def get_num_words(text):
    words = text.split()
    return len(words)

def characters_in_text(text):
    characters_dict = {}
    for ch in text.lower():
        if ch in characters_dict:
            characters_dict[ch] += 1
        else:
            characters_dict[ch] = 1
    return characters_dict

def sort_characters(chars):
    list_of_dict = []
    for char in chars:
        counts = chars[char]
        if char.isalpha() == True:
            list_of_dict.append({"char": char, "num": counts})
    list_of_dict.sort(key=lambda item: item["num"], reverse=True)
    return list_of_dict

    
