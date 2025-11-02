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